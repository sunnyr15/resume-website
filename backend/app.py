from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

# Path to the JSON file that stores view counts
VIEW_COUNT_FILE = 'view_count.json'

# Initialize view count file if it doesn't exist
if not os.path.exists(VIEW_COUNT_FILE):
    with open(VIEW_COUNT_FILE, 'w') as f:
        json.dump({"count": 0}, f)

@app.route('/view-count', methods=['GET'])
def get_view_count():
    with open(VIEW_COUNT_FILE, 'r') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/increment-view', methods=['POST'])
def increment_view_count():
    with open(VIEW_COUNT_FILE, 'r') as f:
        data = json.load(f)

    data['count'] += 1

    with open(VIEW_COUNT_FILE, 'w') as f:
        json.dump(data, f)

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
