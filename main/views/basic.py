from main import app
from flask import Flask, render_template

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/layout', methods = ['POST'])
def layout():
	return render_template('layout.html')


@app.route('/leftSidebar', methods = ['GET'])
def leftSidebar():
	return render_template('leftSidebar.html')

@app.route('/middleSidebar', methods = ['GET'])
def middleSidebar():
	return render_template('middleSidebar.html')

@app.route('/rightSidebar', methods = ['GET'])
def rightSidebar():
	return render_template('rightSidebar.html')	