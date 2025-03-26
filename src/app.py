from flask import Flask, render_template, request


app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/echo-user-input", methods=["POST"])
def echo_user_input():
    return render_template(
        "echo-user-input.html",
        user_input=request.form.get("user-input", "nothing!"),
    )
