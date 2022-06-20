from flask import Blueprint, render_template, Request, url_for

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/login/')
def login():
    return render_template("login.html")

@views.route('/aboutme/')
def aboutme():
    return render_template("aboutme.html")

@views.route('/blog/')
def blog():
    return render_template("blog.html")

@views.route('/contact/')
def contact():
    return render_template("contact.html")

@views.route('/portfolio/')
def portfolio():
    return render_template("portfolio.html")

