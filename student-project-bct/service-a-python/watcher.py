import os
import time
from validator import validate_csv
import requests

def send_data(data):
    url = "http://serviceb:8083/api/students" 

    print("Sending batch size:", len(data))  

    try:
        requests.post(url, json=data)   #send data in json
    except Exception as e:
        print("Error sending:", e)

processed_files = set()

def watch_folder():
    print("Watching folder...")

    while True:
        files = os.listdir("data")

        for file in files:
            if file not in processed_files:
                print(f"Processing {file}")

                valid_data, invalid_data = validate_csv(f"data/{file}")
                send_data(valid_data)

                processed_files.add(file)   

        time.sleep(7)