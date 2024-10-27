from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)  # This will add /metrics endpoint by default

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/')
def home():
    return "Hello from Flask with Prometheus metrics!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
