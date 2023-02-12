from flask import Flask, request, render_template, redirect
import os
from mailer import entry
from dbms import loginHandle


app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/sendMail", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        sub = request.form["sub"]
        body = request.form["down"]
        if file:
            filename = "receipts.csv"
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            entry(sub, body)
    return render_template("sandesh.html")


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if loginHandle(email, password):
            return redirect("/sendMail")
    return render_template("login.html")


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000,debug=False)
