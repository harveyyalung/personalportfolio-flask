from flask import Blueprint, render_template, url_for, request, flash, redirect

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html")

#Pages 

@auth.route('/')
def home():
    return render_template('home.html')

@auth.route('/aboutme/')
def aboutme():
    return render_template("aboutme.html")

@auth.route('/blog/')
def blog():
    return render_template("blog.html")

@auth.route('/contact/')
def contact():
    return render_template("contact.html")

@auth.route('/portfolio/')
def portfolio():
    return render_template("portfolio.html")