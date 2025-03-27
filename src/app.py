from datetime import datetime, timezone
import re
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import requests


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"

db = SQLAlchemy(app)


class WebsiteStatus(db.Model):
    timestamp: datetime = db.Column(
        db.DateTime, primary_key=True, default=datetime.now(timezone.utc)
    )
    url: str = db.Column(db.String(255), nullable=False)
    status: bool = db.Column(db.Boolean, nullable=False)


def is_online(url: str) -> bool:
    return requests.get(url).status_code // 100 == 2


@app.route("/status/<path:url>")
def status(url: str):
    check = re.search("^https?://", url)
    if not check:
        return {"error": "Invalid URL"}

    status = is_online(url)

    website_status = WebsiteStatus(url=url, status=status)
    with app.app_context():
        db.session.add(website_status)
        db.session.commit()

    return {"url": url, "up": status}


@app.route("/")
def home():
    return {"message": "Usage: /status/<url>"}


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run()
