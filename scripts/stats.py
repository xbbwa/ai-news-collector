"""Quick health report over the SQLite database: per-source counts and extraction results."""
import sqlite3
import sys
from pathlib import Path

db = Path(sys.argv[1] if len(sys.argv) > 1 else "data/collector.db")
c = sqlite3.connect(db)

print("extract_status:", c.execute("select extract_status, count(*) from items group by 1").fetchall())
print("\nby source  (total / ok / failed / skipped):")
rows = c.execute(
    """select source_id, count(*),
              sum(extract_status='ok'), sum(extract_status='failed'), sum(extract_status='skipped')
       from items group by 1 order by 2 desc"""
)
for sid, n, ok, failed, skipped in rows:
    print(f"  {sid:<26} {n:>5} {ok:>5} {failed:>5} {skipped:>5}")

print("\ntop extract errors:")
for err, n in c.execute(
    "select substr(extract_error,1,110), count(*) from items where extract_status='failed' group by 1 order by 2 desc limit 10"
):
    print(f"  {n:>4}  {err}")

print("\nsource errors:")
for sid, err in c.execute("select source_id, substr(last_error,1,120) from source_state where last_error is not null"):
    print(f"  {sid:<26} {err}")
