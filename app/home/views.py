from flask import Flask, Blueprint, redirect, render_template, request, session
from app.models import Course


home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def index():
    courses = Course.query.filter_by(is_active=True).all()
    return render_template("/home/index.html", courses=courses)








