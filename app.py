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

@app.route("/users/<name>")
def user_page(name):
    return render_template("index.html", 
                           name=name.title(), role="Pharmacist", city="Taipei")

if __name__ == "__main__":
    app.run()