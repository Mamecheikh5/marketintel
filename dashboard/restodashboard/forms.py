# app/admin/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,RadioField
from wtforms.validators import DataRequired,NumberRange
from wtforms.ext.sqlalchemy.fields import QuerySelectField


class rechercherForm(FlaskForm):
    recherche = StringField('recherche', validators=[DataRequired()])
    filtre = RadioField('filtre', choices=[('0','Tous'),('1','senegal'),('2','bénin'),('3','côte d\'ivoire'),('4','Burkina fasso'),('5','Togo')])
    submit = SubmitField('Submit')
