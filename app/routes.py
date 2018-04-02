from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

#Check
@app.route('/test')
def test():
	return "<h1>test</h1>"