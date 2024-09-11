from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    employee_number = StringField(
        "Employee Number", validators=[DataRequired("We need this please")]
    )
    password = PasswordField("Password", validators=[DataRequired("Password plz")])
    submit = SubmitField("Login")
