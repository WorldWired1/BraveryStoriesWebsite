from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return render_template("Main Page.html")

@app.route("/stories")
def stories():
    return render_template("stories.html")

@app.route("/login")
def login():
    return render_template("Login.html")


app.run(debug=True)
