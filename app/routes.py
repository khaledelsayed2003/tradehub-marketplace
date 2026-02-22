from app import app, db, bcrypt
from flask import render_template, redirect, url_for, flash, request
from app.models import Item, User, load_user
from app.forms import RegisterForm, LoginForm, PurchaseItemForm
from flask_login import login_user, logout_user, login_required, current_user

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route("/market", methods=['GET', 'POST'])
@login_required
def market_page():
    purchase_form = PurchaseItemForm()
    if request.method == 'POST':
        purchased_item = request.form.get('purchased_item')
        purchased_item_obj = Item.query.filter_by(name=purchased_item).first()
        if purchased_item_obj:
            purchased_item_obj.owner = current_user.id 
            current_user.budget -= purchased_item_obj.price
            db.session.commit()
            flash(f'You successfully purchased {purchased_item_obj.name} for ${purchased_item_obj.price}!', category='success')
        return redirect(url_for('market_page'))
    
    items = Item.query.filter_by(owner=None)
    return render_template('market.html', items=items, purchase_form=purchase_form)

@app.route("/register", methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        created_user = User(username=form.username.data, email_address=form.email_address.data, password=form.password.data)
        db.session.add(created_user)
        db.session.commit()
        
        login_user(created_user)
        flash(f"{created_user.username}, your account has been created and you're now logged in 🎉", "success")
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

@app.route("/logout")
def logout_page():
    logout_user()
    flash("Logged out successfully! Come back anytime 🚀", "info")
    return redirect(url_for('home_page'))
    