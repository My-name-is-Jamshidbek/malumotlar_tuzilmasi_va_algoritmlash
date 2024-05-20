import requests
import csv
import datetime
import os


def get_telemetry_data():
    url = "http://thingsboard.k-tech.uz/api/plugins/telemetry/DEVICE/2a88f440-0e91-11ef-af89-d96679404e50/values/timeseries"
    params = {
        "keys": "temperature,humidity,so2,no2,dust"
    }
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1c2VyMTExQGdtYWlsLmNvbSIsInVzZXJJZCI6IjM3Mzg1NmMwLTBlYzUtMTFlZi1hZjg5LWQ5NjY3OTQwNGU1MCIsInNjb3BlcyI6WyJDVVNUT01FUl9VU0VSIl0sInNlc3Npb25JZCI6IjhhZjlhYThkLTk4MjktNGE1Yy04YjM0LTdkZGExOTNlMzNiNiIsImlzcyI6InRoaW5nc2JvYXJkLmlvIiwiaWF0IjoxNzE2MTg2NTk1LCJleHAiOjE3MTYxOTU1OTUsImZpcnN0TmFtZSI6IkFpciIsImxhc3ROYW1lIjoiTW9uaXRvcmluZyIsImVuYWJsZWQiOnRydWUsImlzUHVibGljIjpmYWxzZSwidGVuYW50SWQiOiJkYzkyZTUzMC1lNWU1LTExZWUtYjRmYi02YjVlNzllOWUyMmYiLCJjdXN0b21lcklkIjoiMTA1ZWM1ODAtMGVjNC0xMWVmLWFmODktZDk2Njc5NDA0ZTUwIn0.ljH6CuA3zo_IdlywM2ppb2cCT5orJKJZIoORYNYpc7AF4exp10Q5KVz1QCcaEswbk5ewidlKcETiH6wqalqZnA"
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        print("Telemetry Data:", data)
        write_to_csv(data)
    else:
        print("Failed to fetch data. Status code:", response.status_code)
        print("Response:", response.text)


def write_to_csv(data):
    csv_file = "telemetry_data.csv"
    fields = ['timestamp', 'temperature', 'humidity', 'so2', 'no2', 'dust']

    # Convert timestamp to human-readable format
    for key in data:
        for entry in data[key]:
            entry['ts'] = datetime.datetime.fromtimestamp(entry['ts'] / 1000).strftime('%Y-%m-%d %H:%M:%S')

    file_exists = os.path.isfile(csv_file)

    with open(csv_file, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)

        # Write header only if the file is being created
        if not file_exists:
            writer.writeheader()

        rows = []

        for i in range(len(data['temperature'])):
            row = {
                'timestamp': data['temperature'][i]['ts'],
                'temperature': data['temperature'][i]['value'],
                'humidity': data['humidity'][i]['value'],
                'so2': data['so2'][i]['value'],
                'no2': data['no2'][i]['value'],
                'dust': data['dust'][i]['value'] if i < len(data['dust']) else None
            }
            rows.append(row)

        writer.writerows(rows)

    print(f"Data has been appended to {csv_file}")


if __name__ == "__main__":
    get_telemetry_data()
