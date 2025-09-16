from flask import Flask, render_template, request, redirect, url_for, session, flash
import os

app = Flask(__name__)
app.secret_key = "your-secret-key"  # for sessions, replace with secure key

# Dummy in-memory "database"
users = {}  # {username: password}
user_dbs = {}  # {username: [list of user datasets]}

# Public datasets (everyone can see)
public_datasets = [
    "Global Weather Data",
    "COVID-19 Statistics",
    "World Population Dataset",
    "Stock Market Prices"
]

# --- Routes ---
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uname = request.form["username"]
        pwd = request.form["password"]
        if uname in users and users[uname] == pwd:
            session["user"] = uname
            flash("Login successful!", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid username or password", "danger")
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        uname = request.form["username"]
        pwd = request.form["password"]
        if uname in users:
            flash("User already exists!", "warning")
        else:
            users[uname] = pwd
            user_dbs[uname] = []
            flash("Signup successful! Please login.", "success")
            return redirect(url_for("login"))
    return render_template("signup.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        flash("Please log in first", "warning")
        return redirect(url_for("login"))
    uname = session["user"]
    my_datasets = user_dbs.get(uname, [])
    return render_template("dashboard.html", 
                           public_datasets=public_datasets, 
                           my_datasets=my_datasets, 
                           user=uname)

@app.route("/create", methods=["GET", "POST"])
def create():
    if "user" not in session:
        flash("Please log in first", "warning")
        return redirect(url_for("login"))

    if request.method == "POST":
        dataset_name = request.form["dataset_name"]
        uname = session["user"]
        user_dbs[uname].append(dataset_name)
        flash(f"Dataset '{dataset_name}' created!", "success")
        return redirect(url_for("dashboard"))

    return render_template("create.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("Logged out successfully", "info")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
