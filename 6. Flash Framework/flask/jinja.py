from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def welcome():
    return "<html><body><h1>Welcome to the Flask app</h1></body></html>"


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello, {name}"
    return render_template("form.html")


@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello, {name}"
    return render_template("form.html")


@app.route("/success/<int:score>")
def success(score):
    res = ""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"

    return render_template("result.html", result=res)


@app.route("/successres/<int:score>")
def successres(score):
    res = ""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"

    exp = {"Score": score, "Res": res}
    return render_template("result1.html", results=exp)


@app.route("/getresults", methods=["GET", "POST"])
def getresults():



if __name__ == "__main__":
    app.run(debug=True)
