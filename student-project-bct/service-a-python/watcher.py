import os
import time
from validator import validate_csv
import requests

# 🔥 ADD HERE (TOP LEVEL)
def send_data(data):
    url = "http://localhost:8083/api/students"

    print("Sending data:", data[:2])   # DEBUG

    for student in data:
        try:
            requests.post(url, json=student)
        except Exception as e:
            print("Error sending:", e)


def watch_folder():
    print("Watching folder...")

    while True:
        files = os.listdir("data")

        for file in files:
            print(f"Processing {file}")

            valid_data, invalid_data = validate_csv(f"data/{file}")

            send_data(valid_data)

        time.sleep(5)