# app/home/__init__.py

from flask import Blueprint

home = Blueprint('restaudashboard', __name__)

from . import views