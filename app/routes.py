from app import app, db, bcrypt, mail
from flask import render_template, redirect, url_for, flash, request, session
from app.models import Item, User, load_user
from app.forms import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm, ForgotPasswordForm, VerifyCodeForm
from flask_login import login_user, logout_user, login_required, current_user
from flask_mail import Message
import random
import string

# helper function
def generate_code():
    return ''.join(random.choices(string.digits, k=6))


@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route("/market", methods=['GET', 'POST'])
@login_required
def market_page():
    purchase_form = PurchaseItemForm()
    sell_form = SellItemForm()
    if request.method == 'POST':
        purchased_item = request.form.get('purchased_item')
        purchased_item_obj = Item.query.filter_by(name=purchased_item).first()
        sold_item = request.form.get('sold_item')
        sold_item_obj = Item.query.filter_by(name=sold_item).first()
        
        if purchased_item_obj:
            if current_user.can_afford(purchased_item_obj):
                purchased_item_obj.owner = current_user.id 
                current_user.budget -= purchased_item_obj.price
                db.session.commit()
                flash(f'You successfully purchased {purchased_item_obj.name} for ${purchased_item_obj.price}!', category='success')
            else:
                flash(f"Insufficient budget! {purchased_item_obj.name} costs ${purchased_item_obj.price} but you only have ${current_user.budget}.", category='danger')
        
        if sold_item_obj:
            sold_item_obj.owner = None
            current_user.budget += sold_item_obj.price                                                 
            db.session.commit()
            flash(f'✅ You successfully sold {sold_item_obj.name} for ${sold_item_obj.price}!', category='warning')
             
        return redirect(url_for('market_page'))
    
    items = Item.query.filter_by(owner=None)
    return render_template('market.html', items=items, purchase_form=purchase_form, sell_form=sell_form)

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

@app.route("/delete-account")
@login_required
def delete_account():
    user_to_delete = User.query.filter_by(username=current_user.username).first()
    logout_user()
    db.session.delete(user_to_delete)
    db.session.commit()
    flash('💀 Your account has been permanently deleted. Goodbye!', category='danger')
    return redirect(url_for('home_page'))

@app.route("/forgot-password", methods=['GET', 'POST'])
def forgot_password():
    form = ForgotPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email_address=form.email_address.data).first()
        if user:
            code = generate_code()
            session['reset_code'] = code
            session['reset_email'] = user.email_address

            msg = Message(
                subject="TradeHub — Password Reset Code",
                sender=app.config['MAIL_USERNAME'],
                recipients=[user.email_address]
            )
            msg.body = f"""
Hi {user.username},

Your TradeHub verification code is:

{code}

This code is for resetting your password.
If you didn't request this, ignore this email.

— TradeHub
            """
            mail.send(msg)
            flash(f"A verification code has been sent to {user.email_address}", category='success')
            return redirect(url_for('verify_code'))
        else:
            flash("No account found with that email.", category='danger')

    return render_template('forgot_password.html', form=form)

@app.route("/verify-code", methods=['GET', 'POST'])
def verify_code():
    form = VerifyCodeForm()
    if form.validate_on_submit():
        code = session.get('reset_code')
        if form.code.data == code:
            flash("Code verified successfully! Please set your new password.", category='success')
            return redirect(url_for('reset_password')) 
        else:
            flash("Invalid code. Please check your email and try again.", category='danger')
            
    return render_template('verify_code.html', form=form)
    