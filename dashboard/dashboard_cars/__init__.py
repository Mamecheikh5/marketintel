# app/home/__init__.py

from flask import Blueprint

dashboard_cars = Blueprint('dashboard_cars', __name__)

from . import views