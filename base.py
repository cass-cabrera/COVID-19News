from flask import Flask, render_template
from flask_bootstrap import Bootstrap 

app = Flask(__name__)
bootstrap = Bootstrap(app)
@app.route('/')
def home():
	return render_template('home.html')

@app.route('/whattodo')
def whattodo():
	return render_template('whattodo.html')

@app.route('/mythbusters')
def mythbuster():
	return render_template('mythbuster.html')