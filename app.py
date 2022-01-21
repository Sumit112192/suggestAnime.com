from flask import Flask,render_template,flash,redirect,url_for,session,logging,request

from jikanpy import Jikan
import random

jikan = Jikan()


app=Flask(__name__)






@app.route('/')
def home():
	imageUrl = "https://images.unsplash.com/photo-1613376023733-0a73315d9b06?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80"
	return render_template('index2.html', imageUrl = imageUrl)

@app.route('/data/', methods = ['POST', 'GET'])
def data():
	if request.method == 'GET':
		return "The URL /data is accessed directly. Input the name to see results"

	if request.method == 'POST':
		form_data = request.form
		searches = jikan.search('anime',form_data['name'])
		imageUrl = searches['results'][0]['image_url']
		if imageUrl is not None:
			return render_template('index2.html', imageUrl = imageUrl)
		else:
			return "No data available"
if __name__ == '__main__':
    app.run(debug=True)
