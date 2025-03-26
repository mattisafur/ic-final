from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def index():
    return """
    <form action="/echo-user-input" method="POST">
        <input name="user_input">
        <input type="submit" value="Submit">
    </form>
    """


@app.route("/echo-user-input", methods=["POST"])
def echo_user_input():
    return "You entered: " + request.form.get("user_input", "")
