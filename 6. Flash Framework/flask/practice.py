from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def welcome():
    return "<html><body><h1>Welcome to flask app</h1></body></html>"


@app.route("/index")
def index():
    return render_template("index_prac.html")


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello {name}"
    return render_template("form_prac.html")


@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello {name}"
    return render_template("form_prac.html")

@app.route("/successres/<int:score>", methods=["GET", "POST"])
def successres(score):
    res = ""
    if score >= 50:
        res="Passed"
    else:
        res= "Failed"

    exp = {"score"  : score, "result": res}
    return render_template("successres.html", results=exp)

@app.route("/getresult", methods=["GET", "POST"])
def getresult():
    total_score = 0
    if request.method == "POST":
        science = float(request.form["science"])
        maths = float(request.form["maths"])
        english = float(request.form["english"])
        total_score = science + maths + english
    return render_template("getresult.html")


@app.route("/submit2", methods=["GET", "POST"])
def submit2():
    total_score = 0
    if request.method == "POST":
        science = float(request.form["science"])
        maths = float(request.form["maths"])
        english = float(request.form["english"])
        total_score = science + maths + english
    return "<html><body><h1>Total Score: {}</h1></body></html>".format(total_score)

if __name__ == "__main__":
    app.run(debug=True)
