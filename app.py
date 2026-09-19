from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", 
                           name="Evelyn", 
                           role="Pharmacist", 
                           city="Taipei")

@app.route("/dog")
def dog():
    return "woof"

if __name__ == "__main__":
    app.run()