from flask import Flask, render_template
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from wtforms import Stringfield, PasswordField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'


class LoginForm(FlaskForm):
    username = StringField('username')
    password = PasswordField('password')


@app.route('/form')
def form():
    form = LoginForm()
    return render_template('FormLog.html', form=form)


@app.route('/')
def index():
    return render_template('FormReg.html')


@app.route('/', methods=["post"])
def register():
    return 'Welcome ...'


if __name__ == '__main__':
    app.run(debug=True)
