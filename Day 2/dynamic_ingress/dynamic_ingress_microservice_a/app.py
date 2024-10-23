from flask import Flask
import requests

app = Flask(__name__)

@app.route('/hello')
def hello():
    # Communicate with Microservice C
    response = requests.get('http://dynamic-ingress-microservice-c:5002')
    return f"<h1>Hello from Microservice A!</h1><p>Microservice C says: {response.text}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
