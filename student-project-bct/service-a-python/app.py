from flask import Flask
from generator import generate_csv
from watcher import watch_folder, send_data
from validator import validate_csv
import threading

app = Flask(__name__)

@app.route("/generate")
def generate():
    generate_csv("sample.csv")

    # validate
    valid_data, invalid_data = validate_csv("data/sample.csv")

    # send to Spring Boot
    send_data(valid_data)

    return "CSV Generated & Sent!"

if __name__ == "__main__":
    print("Starting Flask server...")
    threading.Thread(target=watch_folder, daemon=True).start()
    app.run(host="127.0.0.1", port=5000, debug=True)