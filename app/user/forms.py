from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_babel import lazy_gettext

class LoginForm(FlaskForm):
    username = StringField(
        lazy_gettext('Username'),
        validators=[DataRequired(message=lazy_gettext("ユーザ名を入力してください"))],
        render_kw={"placeholder": lazy_gettext("Username")}
    )
    password = PasswordField(
        lazy_gettext('Password'),
        validators=[DataRequired(message=lazy_gettext("パスワードを入力してください"))],
        render_kw={"placeholder": lazy_gettext("Password")}
    )
    submit = SubmitField(lazy_gettext('Login'))

class RegisterForm(FlaskForm):
    username = StringField(
        lazy_gettext('Username'),
        validators=[DataRequired(lazy_gettext("ユーザ名を入力してください"))],
        render_kw={"placeholder": lazy_gettext("Username")}
    )
    password = PasswordField(
        lazy_gettext('Password'),
        validators=[DataRequired(lazy_gettext("パスワードを入力してください"))],
        render_kw={"placeholder": lazy_gettext("Password")}
    )
    submit = SubmitField(lazy_gettext('Register'))