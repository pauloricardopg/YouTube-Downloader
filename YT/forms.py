from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired,Length

class FormLink(FlaskForm):
    link = StringField('Digite o link', validators=[DataRequired(), Length(2, 140)])
    botao_submit = SubmitField('Baixar')