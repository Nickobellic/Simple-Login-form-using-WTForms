from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, PasswordField,SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "avrK2004"


class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(),Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(8,30, message="No.of.Characters should be greater than 8 and less than 30")])
    submit = SubmitField(label="Log In")


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login.html', methods=['GET', 'POST'])
def login():
    form = MyForm()
    if request.method == "POST":
        if form.validate_on_submit():
            return redirect(url_for('succ'))
        else:
            return redirect(url_for('deny'))
    return render_template('login.html', form=form)

@app.route('/fail')
def deny():
    return render_template('denied.html')

@app.route('/success')
def succ():
    return render_template('success.html')




if __name__ == '__main__':
    app.run(debug=True)