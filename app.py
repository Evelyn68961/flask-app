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

@app.route("/patients")
def patients():
    ward = [
        {"name": "Chen", "age": 68, "diagnosis": "COPD"},
        {"name": "Wang", "age": 74, "diagnosis": "CHF"},
        {"name": "Lin",  "age": 55, "diagnosis": "Pneumonia"},
    ]
    return render_template("patients.html", patients=ward)

if __name__ == "__main__":
    app.run()