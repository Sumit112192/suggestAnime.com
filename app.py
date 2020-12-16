from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
import random


app=Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'suggestanime'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
def home():
	cur = mysql.connection.cursor()
	cur.execute("select count(wallpaperid) as total from wallpapers")
	total = cur.fetchone()
	wallpaperid = random.randint(1,total['total'])
	cur.execute('select linkid from wallpapers where wallpaperid = (%s)', (wallpaperid,))
	linkid = cur.fetchone()
	linkid = linkid['linkid']
	imageUrl = "https://drive.google.com/uc?export=view&id="+linkid
	return render_template('index.html', imageUrl = imageUrl)

if __name__ == '__main__':
    app.run(debug=True)