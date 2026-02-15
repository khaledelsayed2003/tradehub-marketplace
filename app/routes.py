from app import app, db
from flask import render_template, redirect, url_for
from app.models import Item, User
from app.forms import RegisterForm

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
        created_user = User(username=form.username.data, email_address=form.email_address.data, password_hash=form.password.data)
        db.session.add(created_user)
        db.session.commit()
        return redirect(url_for('market_page'))
    return render_template('register.html', form=form)