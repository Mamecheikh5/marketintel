# app/auth/__init__.py

from flask import Blueprint

acceuil = Blueprint('acceuil', __name__)

from . import views