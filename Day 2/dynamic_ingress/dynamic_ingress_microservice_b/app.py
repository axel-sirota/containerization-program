from flask import Flask
import requests

app = Flask(__name__)

@app.route('/post')
def post():
    # Communicate with Microservice C
    response = requests.get('http://dynamic-ingress-microservice-c:5002')
    return f"<h1>Post from Microservice B!</h1><p>Microservice C says: {response.text}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
