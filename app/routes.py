from app import app, db, bcrypt
from flask import render_template, redirect, url_for, flash
from app.models import Item, User
from app.forms import RegisterForm, LoginForm
from flask_login import login_user

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

@app.route("/register", methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        created_user = User(username=form.username.data, email_address=form.email_address.data, password=form.password.data)
        db.session.add(created_user)
        db.session.commit()
        
        flash("Account created successfully 🎉", category="success")
        return redirect(url_for('market_page'))
    
    if form.errors != {}:
        for field, error_msg in form.errors.items():
            flash(f"{field.replace('_',' ').title()}: {error_msg}", category="danger")
            
    return render_template('register.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        authenticated_user = User.query.filter_by(username=form.username.data).first()
        if authenticated_user and authenticated_user.check_password_of_authenticated_user(authenticated_password=form.password.data):
            login_user(authenticated_user)
            flash(f"Welcome back {authenticated_user.username}! You logged in successfully ✨", category="success")
            return redirect(url_for('market_page'))
        else:
            flash("Oops! 😕 The username or password you entered is incorrect.", "danger")
            
    return render_template('login.html', form=form)
    