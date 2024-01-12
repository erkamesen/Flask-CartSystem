from flask import Blueprint, request, flash, render_template, redirect, url_for
from .forms import LoginForm, RegisterForm
from app.models import User
from flask_login import current_user, login_user, logout_user, login_required
from app import db

user_bp = Blueprint("_user", __name__)


@user_bp.route("/register", methods=["GET", "POST"])
def user_register():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
    form = RegisterForm()
    
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        
        db.session.add(user)
        db.session.commit()
        flash('Registered Succesfully!!')
        return redirect(url_for('_user.user_login'))
    else:
        return render_template("user/register.html", form=form)
    
    
@user_bp.route("/login", methods=["GET", "POST"])
def user_login():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('_user.user_login'))
        login_user(user)
        return redirect(url_for('home.index'))
    else:
        return render_template("user/login.html", form=form)


@login_required
@user_bp.route('/logout')
def user_logout():
    logout_user()
    return redirect(url_for('home.index'))
        
        
        
