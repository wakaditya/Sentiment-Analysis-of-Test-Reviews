from flask import Flask, render_template, flash, request, jsonify
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from label import *
from score import *


# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])


@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
    x = []
    if request.method == 'POST':
        name = request.form['name']
        # json = JSON.parse(request.body)
        # json["review"]
        print(name)

        if form.validate():
            x = get_score(name)
            print(x)
            flash(x)
            y = get_label(name)
            print(y)
            flash(y)

        else:
            flash('All the form fields are required. ')

            # requests.post('MINERVA_URL', data = {'score':'value', 'label' :'value'})

    return render_template('hello.html', form = form)


if __name__ == "__main__":
    app.run()
