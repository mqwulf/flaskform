from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def receive_data():
    name = request.form["username"]
    password = request.form["password"]
    return f"<h1>Name: {name}</h1><h1>Password: {password}</h1>"

if __name__ == "__main__":
    app.run(port=8000, debug=True)