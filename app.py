from flask import Flask, Response

app = Flask(__name__)


@app.get("/")
def index():
    return "hello world"

if __name__ == "__main__":
    app.run(host="localhost", debug=True, port=5000)
