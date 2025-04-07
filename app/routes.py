from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from . import app, db
from .models import User
from .forms import LoginForm, SignupForm

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:  
            login_user(user)
            return redirect(url_for("home"))
        flash("Invalid credentials", "danger")
    return render_template("login.html", form=form)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Account created!", "success")
        return redirect(url_for("login"))
    return render_template("signup.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))
