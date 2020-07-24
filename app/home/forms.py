# app/admin/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField


class rechercherForm(FlaskForm):
    recherche = StringField('recherche', validators=[DataRequired()])
    submit = SubmitField('Submit')
