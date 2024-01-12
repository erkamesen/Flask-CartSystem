from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.models import Course, Cart, CartItem, User
from flask_login import login_required, current_user
from app import db

course_bp = Blueprint("_course", __name__, url_prefix="/courses/")


@course_bp.route("<int:id>/")
def course_detail(id):
    course = Course.query.get(id)
    return render_template("product/course-detail.html", course=course)



@login_required
@course_bp.route("add-to-cart/<int:id>/")
def add_to_cart(id):
    
    if not current_user.is_authenticated:
        return redirect(url_for("_user.user_login"))
    user_cart = Cart.query.filter_by(user_id=current_user.id).first()
    if not user_cart:
        user_cart = Cart(user_id=current_user.id)
        db.session.add(user_cart)
        db.session.commit()
    cart_item = CartItem.query.filter_by(cart_id=user_cart.id, course_id=id).first()

    if cart_item:
        flash("The course is already in the cart.", "info")
        return redirect(url_for("home.index"))

    course = Course.query.get(id)
    new_cart_item = CartItem(cart_id=user_cart.id, course_id=course.id)
    db.session.add(new_cart_item)
    db.session.commit()

    flash("Course added..", "success")
    return redirect(url_for("_course.cart"))


    
@login_required
@course_bp.route("/remove-from-cart/<int:id>/")
def remove_from_cart(id):
    if not current_user.is_authenticated:
        return redirect(url_for("_user.user_login"))
    user_cart = Cart.query.filter_by(user_id=current_user.id).first()

    if not user_cart:
        flash("Cart is empty.", "warning")
        return redirect(url_for("home.index"))

    cart_item = CartItem.query.filter_by(cart_id=user_cart.id, course_id=id).first()

    if not cart_item:
        flash("Course not in cart.", "warning")
        return redirect(url_for("home.index"))

    db.session.delete(cart_item)
    db.session.commit()

    flash("Course removed from cart.", "success")
    return redirect(url_for("_course.cart"))

@login_required
@course_bp.route("/cart")
def cart():
    if not current_user.is_authenticated:
        return redirect(url_for("_user.user_login"))
    user_cart = Cart.query.filter_by(user_id=current_user.id).first()
    if not user_cart:
        flash("Cart is empty.", "warning")
        return redirect(url_for("home.index"))
    cart_items = [Course.query.get(cart.course_id) for cart in CartItem.query.filter_by(cart_id=user_cart.id).all()]
    return render_template("product/cart.html", cart_items=cart_items)