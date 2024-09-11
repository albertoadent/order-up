from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    employee_number = StringField(
        "Employee Number", validators=[DataRequired("We need this please")]
    )
    password = PasswordField("Password", validators=[DataRequired("Password plz")])
    submit = SubmitField("Login")

class TableAssignmentForm(FlaskForm):
    tables = SelectField("Tables", coerce=int)
    servers = SelectField("Servers", coerce=int)
    assign = SubmitField("Assign")