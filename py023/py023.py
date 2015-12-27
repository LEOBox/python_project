import sqlite3
from flask import Flask,request,session,g,redirect,url_for,abort,render_template,flash
from contextlib import closing

#configuration
DATABASE = '/tmp/py023.db'
DEBUG = True
SECRET_KEY = 'develop key'
USERNAME = 'root'
PASSWORD = 'root'

app = Flask(__name__)
app.config.from_object(__name__)

def initDB():
	with closing(connectDB()) as db:
		with app.open_resource('schema.sql') as f:
			db.cursor().executescript(f.read())
		db.commit()

@app.before_request
def before_request():
	g.db = connectDB()

@app.teardown_request
def teardown_request(exception):
	g.db.close()

def connectDB():
	return sqlite3.connect(app.config['DATABASE'])

@app.route('/')
def show_entries():
	cur = g.db.execute('select user,comment from entries order by id desc')
	entries = [dict(user = row[0],comment = row[1]) for row in cur.fetchall()]
	return render_template('show_entries.html',entries=entries)

@app.route('/add',methods = ['POST'])
def addEntry():
	g.db.execute('insert into entries (user, comment) values (?, ?)',[request.form['user'],request.form['comment']])
	g.db.commit()
	flash('New comment was post')
	return redirect(url_for('show_entries'))

if __name__ == '__main__':
	app.run()