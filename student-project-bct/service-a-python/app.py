from flask import Flask
from generator import generate_csv
from watcher import watch_folder, send_data
from validator import validate_csv
from flask_cors import CORS
from flask import Flask, render_template
import threading

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate")
def generate():
    print("API HIT ")   

    generate_csv("sample.csv")

    valid_data, invalid_data = validate_csv("data/sample.csv")

    send_data(valid_data)

    return {
    "valid_count": len(valid_data),
    "invalid_count": len(invalid_data)
    }
if __name__ == "__main__":
    print("Starting Flask server...")
    threading.Thread(target=watch_folder, daemon=True).start()
    app.run(host="0.0.0.0", port=5000)