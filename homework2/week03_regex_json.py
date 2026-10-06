import json, re, csv
from pathlib import Path

DATA = Path(__file__).parents[1] / "datasets" / "events.jsonl"
OUTPUT = Path(__file__).parent / "failed_events.csv"

IP_RE = re.compile(
    r"^(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)"
    r"(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}$"
)


def main():
    total_events = 0
    failed_events = []

    with open(DATA, "r", encoding="utf-8") as file:
        for line in file:
            if not line.strip():
                continue

            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                print("Geçersiz JSON satırı atlandı.")
                continue

            total_events += 1

            if event.get("status") == "FAILED":
                ip = event.get("src_ip", "")

                if IP_RE.fullmatch(ip):
                    failed_events.append(event)

    with open(OUTPUT, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = [
            "timestamp",
            "event_id",
            "src_ip",
            "user",
            "status"
        ]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for event in failed_events:
            writer.writerow({
                "timestamp": event.get("timestamp", ""),
                "event_id": event.get("event_id", ""),
                "src_ip": event.get("src_ip", ""),
                "user": event.get("user", ""),
                "status": event.get("status", "")
            })

    print("Total events:", total_events)
    print("Failed events:", len(failed_events))
    print("CSV oluşturuldu: failed_events.csv")


if __name__ == "__main__":
    main()