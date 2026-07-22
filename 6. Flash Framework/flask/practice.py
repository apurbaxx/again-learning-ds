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


if __name__ == "__main__":
    app.run(debug=True)
