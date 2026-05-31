from flask import Flask

app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to this Flask server..."


@app.route("/index")
def greet():
    return "Welcome to the index page"


if __name__ == "__main__":
    app.run(debug=True)
