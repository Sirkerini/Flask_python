from flask import Flask, render_template, redirect, url_for, session, request

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=("GET","POST"))
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        return redirect(url_for("perfil"))
     
    return render_template("login.html")


@app.route("/perfil")
def perfil():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)