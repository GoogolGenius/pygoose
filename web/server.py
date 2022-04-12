from flask import Flask
from threading import Thread

app = Flask("PyGoose Pre-Alpha")


@app.route("/")
def home():
    return "Server Status: Online. PyGoose Developed by GoogleGenius#3876 and Texas Red#0162. Invite at https://pygoose.webflow.io."


def run():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()
