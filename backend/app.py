from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "SYSTEM HEALTH OK - ALL SYSTEMS GO"})

@app.route('/metrics')
def metrics():
    return jsonify({
        "cpu": random.randint(1, 100),
        "memory": random.randint(1, 100)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
