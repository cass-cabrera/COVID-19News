from flask import Flask, render_template, request
import requests, json
from flask_bootstrap import Bootstrap 
from api import getStat, getKeys, getWorld

app = Flask(__name__)
bootstrap = Bootstrap(app)

#the route for the home page
@app.route('/')
def home():
	return render_template('home.html',
		options = getKeys(),
		world = getWorld()
		)

#the route for the what to do page
@app.route('/whattodo')
def whattodo():
	return render_template('whattodo.html')

#the route for the mythbusters page
@app.route('/mythbusters')
def mythbuster():
	return render_template('mythbuster.html')

#the route for redirecting the search
@app.route('/search', methods=['GET']) 
def search():
	country = request.args.get('region')
	data = getStat(country)
	return render_template('home.html',
		data = data["data"]["summary"],
		options = getKeys(), 
		country = country
		)
