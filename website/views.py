from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
# from .models import Post, User, Comment, Like
# from . import db

views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template("temp-view.html")