from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Communicate with Microservice B
    response = requests.get('http://microservice-b:5001')
    return f"<h1>Microservice A</h1><p>Microservice B says: {response.text}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
