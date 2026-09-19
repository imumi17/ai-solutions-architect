import argparse
import json
from collections import Counter

def parse_line(line):
    parts = line.split()

    date = parts[0]
    time = parts[1]
    ip = parts[2]
    method = parts[3]
    endpoint = parts[4]
    status = int(parts[5])
    latency = float(parts[6].replace("ms", ""))

    return {
        "timestamp": f"{date} {time}",
        "ip": ip,
        "method": method,
        "endpoint": endpoint,
        "status": status,
        "latency": latency
    }


def analyze_logs(
    filename,
    slow_threshold=None,
    status_filter=None,
    ip_filter=None,
    endpoint_filter=None
):
    request_count = 0
    error_count = 0
    malformed_count = 0

    total_latency = 0
    max_latency = 0
    
    slow_requests = []

    endpoint_counter = Counter()
    ip_counter = Counter()
    status_counter = Counter()

    with open(filename, "r") as file:
        for line in file:
            try:
                record = parse_line(line)

                if status_filter is not None and record["status"] != status_filter:
                    continue

                if ip_filter is not None and record["ip"] != ip_filter:
                    continue

                if endpoint_filter is not None and record["endpoint"] != endpoint_filter:
                    continue

                if slow_threshold is not None and record["latency"] > slow_threshold:
                    slow_requests.append(record)

                request_count += 1

                if record["status"] >= 400:
                    error_count += 1

                total_latency += record["latency"]

                if record["latency"] > max_latency:
                    max_latency = record["latency"]

                endpoint_counter[record["endpoint"]] += 1
                ip_counter[record["ip"]] += 1
                status_counter[record["status"]] += 1

            except (ValueError, IndexError):
                malformed_count += 1

    average_latency = (
        total_latency / request_count
        if request_count > 0
        else 0
    )

    return {
        "requests": request_count,
        "errors": error_count,
        "malformed": malformed_count,
        "average_latency": average_latency,
        "max_latency": max_latency,
        "endpoints": endpoint_counter,
        "ips": ip_counter,
        "status_codes": status_counter,
        "slow_requests": slow_requests
    }




def print_report(stats, top):
    print("========================================")
    print("          CLI LOG ANALYZER")
    print("========================================")

    print(f"\nTotal Requests       : {stats['requests']}")
    print(f"Total Errors         : {stats['errors']}")
    print(f"Malformed Lines      : {stats['malformed']}")
    print(f"Average Latency      : {stats['average_latency']:.2f} ms")
    print(f"Max Latency          : {stats['max_latency']:.2f} ms")

    if stats["slow_requests"]:
        print("\nSlow Requests")
        print("----------------------------------------")

    for record in stats["slow_requests"]:
        print(
            f"{record['method']:<6} "
            f"{record['endpoint']:<20} "
            f"{record['status']:<5} "
            f"{record['latency']:.2f} ms"
        )

    print("\nTop Endpoints")
    print("----------------------------------------")

    for endpoint, count in stats["endpoints"].most_common(top):
        print(f"{endpoint:<20} {count}")

    print("\nTop IPs")
    print("----------------------------------------")

    for ip, count in stats["ips"].most_common(top):
        print(f"{ip:<20} {count}")

    print("\nStatus Code Distribution")
    print("----------------------------------------")

    for status, count in stats["status_codes"].most_common():
        print(f"{status:<20} {count}")

def print_json_report(stats):
    output = {
        "requests": stats["requests"],
        "errors": stats["errors"],
        "malformed": stats["malformed"],
        "average_latency": stats["average_latency"],
        "max_latency": stats["max_latency"],
        "endpoints": dict(stats["endpoints"]),
        "ips": dict(stats["ips"]),
        "status_codes": dict(stats["status_codes"]),
        "slow_requests": stats["slow_requests"]
    }

    print(json.dumps(output, indent=4))


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Analyze application logs and generate statistics."
    )

    parser.add_argument(
        "filename",
        help="Path to the application log file"
    )

    parser.add_argument(
        "--top",
        type=int,
        default=5,
        help="Number of top endpoints and IPs to display"
    )

    parser.add_argument(
        "--slow",
        type=float,
        help="Show requests slower than the specified latency in milliseconds"
    )

    parser.add_argument(
    "--status",
    type=int,
    help="Filter requests by HTTP status code"
    )

    parser.add_argument(
    "--ip",
    help="Filter requests by IP address"
    )

    parser.add_argument(
    "--endpoint",
    help="Filter requests by API endpoint"
    )

    parser.add_argument(
    "--json",
    action="store_true",
    help="Output results as JSON"
    )   

    return parser.parse_args()




def main():
    args = parse_arguments()

    try:
        stats = analyze_logs(
            args.filename,
            args.slow,
            args.status,
            args.ip,
            args.endpoint
        )

    except FileNotFoundError:
        print(f"Error: File '{args.filename}' not found.")
        return

    if args.json:
        print_json_report(stats)
    else:
        print_report(stats, args.top)


if __name__ == "__main__":
    main()