from flask import Flask, jsonify, make_response, request, url_for, render_template, redirect, send_from_directory
from werkzeug import secure_filename
from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING
from main import app
import json, csv
from bson import BSON
from bson import json_util
from bson.son import SON
import os

app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['csv'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

def readFile(f):
	header = []
	l = list(f)
	header = []
	data = []
	for i in range(len(l)):
		if i == 0:
			header = l[i]
		else:
			data.append(l[i])
	count = len(header)
	print count
	return header, data, count

@app.before_first_request
def createIndexOnDb():
	""" This function create connection to database on first request
	"""
	client = MongoClient('127.0.0.1:27017')
	db = client['Visualization']
	collection = db['UsersFile']
	return collection


@app.route('/file_upload', methods=['GET','POST'])
def fileUpload():
	if request.method == 'POST':
		
		f = request.files['file']
		if f and allowed_file(f.filename):
		    filename = secure_filename(f.filename)
   		    f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		return redirect(url_for('fileUpload',files = filename))

	if request.method == 'GET':

		filename = request.args.get('files')
	
		with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'rb') as f:
			csvFile = csv.reader(f)
			head, data, count = readFile(csvFile)
			return render_template('leftSidebar.html', files=filename, header = head, d=data, cols = head, headCount = count)
	