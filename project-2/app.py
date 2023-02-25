import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///database.db")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/math")
def math():
    return render_template("math.html")

@app.route("/ict")
def ict():
    return render_template("ict.html")

@app.route("/teachers")
def teachers():
    return render_template("teachers.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

# Bagian untuk routing halaman register
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Jika request nya bernilai "GET" maka pergi ke halaman register dengan tampilan /templates/register.html
    if request.method == "GET":
        return render_template("register.html")

    else:
        # mendefinisikan usernme, password dan confirmation dari request.form.get name di html register
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Jika username = kosong maka munculkan apology Username can't be empty
        # reference: https://stackoverflow.com/questions/9926446/how-to-check-whether-a-strvariable-is-empty-or-not
        if username == '':
            return apology("Username can't be empty")

        # Jika password = kosong maka munculkan apology Password can't be empty
        # reference: https://stackoverflow.com/questions/9926446/how-to-check-whether-a-strvariable-is-empty-or-not
        if password == '':
            return apology("Password can't be empty")

        # Jika confirmation = kosong maka munculkan apology Confirm password can't be empty
        # reference: https://stackoverflow.com/questions/9926446/how-to-check-whether-a-strvariable-is-empty-or-not
        if confirmation == '':
            return apology("Confirm password can't be empty")

        # Jika password tidak sama dengan confirmation maka munculkan apology Password didn't match
        if password != confirmation:
            return apology("Password didn't match")

        # Mengecek inputan form username apakah ada yang sama dengan data di users.username
        matches = db.execute("SELECT * FROM users WHERE username = ?", username)

        # Jika inputan form username ada yang sama dalam users.username (kondisi matches terpenuhi) maka tampilkan apology username not available
        if matches:
            return apology("Username not available")

        # Jika inputan form username TIDAK ada yang sama dalam users.username (kondisi matches TIDAK terpenuhi) maka eksekusi newuser (teruskan eksekusi registrasi ke database)
        else:
            newuser = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, generate_password_hash(password))

        # Membuat session untuk user_id kepada newuser
        session["user_id"] = newuser

        # Memberikan return ke "/" setelah semua alur di atas selesai dijalankan
        return redirect("/")

@app.route("/submit")
def submit():
    return render_template("submit.html")




