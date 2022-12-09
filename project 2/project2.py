
from flask import Flask, render_template, flash, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'project2'
bootstrap = Bootstrap5(app)

class SearchForm(FlaskForm):
    search= StringField("Search for a product", validators=[DataRequired()])

product = []
def store_product(my_product):
	product.append(dict(
    	item = my_product,
      test2 = "sup my boy"
))

@app.route('/', methods=('GET', 'POST'))
def index():
    form = SearchForm()
    if form.validate_on_submit():
        store_product(form.search.data)
        return redirect('/search')
    return render_template('index.html', form=form)





@app.route('/search')
def hello():

   return render_template('search.html', product = product)



