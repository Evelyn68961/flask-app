from flask import Flask, render_template, request, abort

app = Flask(__name__)

WARD = [
    {"name": "Chen", "age": 68, "diagnosis": "COPD"},
    {"name": "Wang", "age": 74, "diagnosis": "CHF"},
    {"name": "Lin",  "age": 55, "diagnosis": "Pneumonia"},
]

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
    return render_template("patients.html", patients=WARD)

@app.route("/patients/<name>")
def patient_detail(name):
    match = next((p for p in WARD if p["name"].lower() == name.lower()), None)
    if match is None:
        abort(404)
    return render_template("patient_detail.html", patient=match)

@app.route("/crcl", methods=["GET", "POST"])
def crcl():
    if request.method == "GET":
        return render_template("crcl_form.html")

    # POST: process the form
    try:
        age = int(request.form["age"])
        sex = request.form["sex"]
        weight = float(request.form["weight"])
        scr = float(request.form["scr"])

        if age <= 0 or weight <= 0 or scr <= 0:
            raise ValueError("All numeric values must be positive.")
        if sex not in ("male", "female"):
            raise ValueError("Please select a sex.")

    except (ValueError, KeyError) as err:
        return render_template("crcl_error.html", error=str(err))

    # Cockcroft-Gault formula
    crcl_value = ((140 - age) * weight) / (72 * scr)
    if sex == "female":
        crcl_value *= 0.85

    return render_template(
        "crcl_result.html",
        crcl=round(crcl_value, 1),
        age=age,
        sex=sex,
        weight=weight,
        scr=scr,
    )

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(error):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run()