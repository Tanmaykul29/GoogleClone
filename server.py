from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/images.html")
def images():
    return render_template("images.html")

@app.route("/advanced.html")
def advance():
    return render_template("advanced.html")
if __name__ == "__main__":
    app.run(debug=True)