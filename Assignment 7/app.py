from flask import Flask, render_template
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'


class LoginForm(FlaskForm):
    username = StringField('username' , validators=[InputRequired()])
    password = PasswordField('password' , validators=[InputRequired()])


@app.route('/form', methods=['GET', 'POST'])
def form():
    form = LoginForm()
    return render_template('FormLog.html', form=form)




@app.route('/', methods=["post"])
def register():
    return 'Welcome ...'


if __name__ == '__main__':
    app.run(debug=True)
