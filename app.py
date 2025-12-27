from flask import Flask, render_template, request, redirect, session
import sqlite3
import random
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# ---------- SECRET KEY ----------
app.secret_key = os.environ.get("SECRET_KEY", "fallback-secret")

# ---------- DATABASE SETUP ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")

def get_db():
    return sqlite3.connect(DB_PATH)

def init_db():
    db = get_db()
    cur = db.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        profile_name TEXT NOT NULL,
        wins INTEGER DEFAULT 0,
        lost INTEGER DEFAULT 0,
        score INTEGER DEFAULT 0
    )
    """)
    db.commit()
    db.close()

# Initialize DB on startup
init_db()

# ---------------- HOME ----------------
@app.route("/")
def home():
    return redirect("/register")

# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_id = request.form["user_id"]
        password = request.form["password"]

        db = get_db()
        cur = db.cursor()
        cur.execute("SELECT password FROM users WHERE user_id=?", (user_id,))
        row = cur.fetchone()
        db.close()

        if row and check_password_hash(row[0], password):
            session["user"] = user_id
            return redirect("/game")
        else:
            return render_template("login.html", error="Invalid login details")

    return render_template("login.html")

# ---------------- REGISTER ----------------
@app.route("/register", methods=["GET", "POST"])
def register():
    error = None   # ✅ ALWAYS define it

    if request.method == "POST":
        user_id = request.form["user_id"]
        password = generate_password_hash(request.form["password"])
        pname = request.form["pname"]

        db = get_db()
        cur = db.cursor()

        cur.execute("SELECT user_id FROM users WHERE user_id=?", (user_id,))
        if cur.fetchone():
            db.close()
            error = "User already exists"
        else:
            cur.execute(
                "INSERT INTO users (user_id, password, profile_name) VALUES (?, ?, ?)",
                (user_id, password, pname)
            )
            db.commit()
            db.close()
            return redirect("/login")

    return render_template("register.html", error=error)


# ---------------- GAME ----------------
@app.route("/game", methods=["GET", "POST"])
def game():
    if "user" not in session:
        return redirect("/login")

    db = get_db()
    cur = db.cursor()

    cur.execute(
        "SELECT wins, lost, score FROM users WHERE user_id=?",
        (session["user"],)
    )
    wins, lost, score = cur.fetchone()

    result = ""
    user_choice = ""
    comp_choice = ""

    if request.method == "POST":
        user_choice = request.form["choice"]
        comp_choice = random.choice(["rock", "paper", "scissors"])

        if user_choice == comp_choice:
            result = "Draw"
        elif (
            (user_choice == "rock" and comp_choice == "scissors") or
            (user_choice == "paper" and comp_choice == "rock") or
            (user_choice == "scissors" and comp_choice == "paper")
        ):
            result = "You Win"
            cur.execute(
                "UPDATE users SET wins=wins+1, score=score+10 WHERE user_id=?",
                (session["user"],)
            )
        else:
            result = "You Lose"
            cur.execute(
                "UPDATE users SET lost=lost+1 WHERE user_id=?",
                (session["user"],)
            )

        db.commit()

    db.close()

    return render_template(
        "game.html",
        wins=wins,
        lost=lost,
        score=score,
        result=result,
        user_choice=user_choice,
        comp_choice=comp_choice
    )

# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

if __name__ == "__main__":
    app.run()
