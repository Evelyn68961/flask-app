from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/dog")
def dog():
    return "woof"

if __name__ == "__main__":
    app.run()