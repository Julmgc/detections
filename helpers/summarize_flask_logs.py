import json
import sys
from collections import Counter

if len(sys.argv) != 2:
    print(f"Usage: python3 {sys.argv[0]} <logfile>")
    sys.exit(1)

logfile = sys.argv[1]

srcips = Counter()
paths = Counter()
statuses = Counter()
queries = Counter()

with open(logfile, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue

        srcips[event.get("srcip", "unknown")] += 1
        paths[event.get("path", "unknown")] += 1
        statuses[str(event.get("status", "unknown"))] += 1

        qs = event.get("query_string", "")
        if qs:
            queries[qs] += 1

print("\n=== Top Source IPs ===")
for value, count in srcips.most_common(5):
    print(f"{value}: {count}")

print("\n=== Top Paths ===")
for value, count in paths.most_common(10):
    print(f"{value}: {count}")

print("\n=== Top Status Codes ===")
for value, count in statuses.most_common(10):
    print(f"{value}: {count}")

print("\n=== Top Query Strings ===")
for value, count in queries.most_common(10):
    print(f"{value}: {count}")
