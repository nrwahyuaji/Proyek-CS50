import os

from flask import Flask, render_template, url_for, redirect, request
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup
from cs50 import SQL

# Configure application
app = Flask(__name__)

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/math")
def math():
    return render_template("math.html")

@app.route("/ict")
def ict():
    return render_template("ict.html")

@app.route("/teachers")
def teachers():
    return render_template("teachers.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Pendaftaran Peserta"""
    if (request.method == "POST"):
        username = request.form.get('username')
        password = request.form.get('password')
        confirmation = request.form.get('confirmation')

        if not username:
            return apology('Isikan nama yang benar!')
        elif not password:
            return apology('Isikan password yang benar!')
        elif not confirmation:
            return apology('Isikan konfirmasi password yang benar!')

        if password != confirmation:
            return apology('Password tidak sama!')

        hash = generate_password_hash(password)

        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)
            return redirect('/')
        except:
            return apology('Telah terdaftar!')

    else:
        return render_template("register.html")


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/submit")
def submit():
    return render_template("submit.html")




