from app import app
from flask import render_template,flash,redirect,url_for
from app.forms import LoginForm

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return url_for('home')
    return render_template('login.html',title='Sign In',form=form)