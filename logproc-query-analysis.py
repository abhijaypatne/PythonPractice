from collections import defaultdict

import requests
import csv


# source: GRAFANA or KIBANA
def get_data(source: str):
    url = "http://localhost:3080/search"
    data = {
        "label_predicates": [
            {"kind": "exact", "field_path": "k8s_namespace", "value": "elasticsearch-config"},
            {"kind": "exact", "field_path": "k8s_environment", "value": "production"},
            {"kind": "exact", "field_path": "k8s_container", "value": "loadtest"}
        ],
        "field_predicates": [
            {"kind": "partial", "field_path": "payload.text", "value": "search completed"},
            {"kind": "exact", "field_path": "payload.json.QueryType", "value": source}
        ],
        "min_time": "2023-10-10T11:58:50Z",
        "max_time": "2023-10-12T11:59:56Z",
        "sort": "Desc",
        "limit": 5000,
        "family": "container_logs"
    }
    response = requests.post(url, json=data)

    json_data = response.json()
    print(json_data["stats"])

    results = json_data["results"]
    print("source: " + source + "; number of results: " + str(len(results)))

    # Initialize the map
    result_map = defaultdict(list)
    result_map2 = defaultdict()
    for result in results:
        try:
            total_duration = result["payload"]["json"]["total_duration_millis"]
            query = result["payload"]["json"]["Query"]
            result_map[total_duration].append(query)
            result_map2[total_duration] = query
        except KeyError:
            print("keyerror: " + str(result))

    sorted_map = dict(sorted(result_map.items(), key=lambda x: x[0], reverse=True))
    sorted_map2 = dict(sorted(result_map2.items(), key=lambda x: x[0], reverse=True))

    # for key, value in sorted_map.items():
    #     print(key, value)

    # Write the key-value pairs to a CSV file
    with open(source + "output.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["total_duration_millis", "Query", "Source"])  # Write header row
        for key, value in sorted_map.items():
            writer.writerow([key, value, source])

    # Write the key-value pairs to a CSV file
    with open(source + "output2.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["total_duration_millis", "Query", "Source"])  # Write header row
        for key, value in sorted_map2.items():
            writer.writerow([key, value, source])


def main():
    get_data("GRAFANA")
    get_data("KIBANA")


if __name__ == "__main__":
    main()
