# app/auth/__init__.py

from flask import Blueprint

home = Blueprint('restodashboard', __name__)

from . import views
