from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
 return '<h1>Hello World!</h1>'
if __name__ == '__main__':
 app.run(debug = True)
 
 #######
 from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
 return '<h1>Hello World!</h1>'
@app.route('/index/<name>')
def hello(name):
 return '<h1>Hello, %s!</h1>' % name
if __name__ == '__main__':
 app.run(debug = True)
 ################3
 
 from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
 return '<h1>Hello World!</h1>'
@app.route('/index/<name>')
def hello(name):
 return render_template('index.html', name = name)
if __name__ == '__main__':
 app.run(debug = True)
 #########
 from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
class NameForm(Form):
 name = TextField('What is your name?', validators = [ Required() ])
@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
 name = None
form = NameForm()
if form.validate_on_submit():
 name = form.name.data
form.name.data = ''
   return render_template('index.html', form = form, name = name)
######################33
{% extends "bootstrap_responsive.html" %}
{% import "bootstrap_wtf.html" as wtf %}
{% block body_content %}
<div class="container">
<div class="page-header">
{% if name %}
<h1>Hello, {{ name }}!</h1>
{% endif %}
</div>
{{ wtf.quick_form(form) }}
</div>
{% endblock %}

