from pymongo import MongoClient
import pymongo
import json
import csv
from mongo_db_connect import db
from scipy.stats.stats import pearsonr
from datetime import datetime

items = db.topics.find({ 'classification' : 'Academic' }, no_cursor_timeout=True)

pp = []

for item in items:
	numOps = 0
	dates = []

	tId = item['_id']
	topicName = item['topicName']
	topicDescription = item['topicDescription']
	semester = item['semester']
	classification = item['classification']
	totalPosts = item['TotalPosts']
	numStudents = item['NumUniqueStudents']
	numInstructors = item['NumUniqueInstructors']
	numTas = item['NumUniqueTas']
	numStudentPosts = item['NumStudentPosts']
	numInstructorPosts = item['NumInstructorPosts']
	numTaPosts = item['NumTaPosts']
	postsPerStudent = item['postsPerStudent']
	postsPerInstructor = item['postsPerInstructor']

	postsInTopic = db.discuss.find({ 'topicId' : tId }, no_cursor_timeout=True)
	
	for p in postsInTopic:
		datePosted = p['datePosted']
		dates.append(datePosted)
		parentPostId = p['parentPostId']
		if parentPostId == None:
			numOps += 1
			ouId = p['d2lid']

	first = min(dates)
	last = max(dates)
	d1 = datetime.strptime(first[0:10], "%Y-%m-%d")
	d2 = datetime.strptime(last[0:10], "%Y-%m-%d")
	duration = abs((d2 - d1).days)

	if numStudents > 0:
		opPerStudent = float(numOps) / float(numStudents)
	else:
		opPerStudent = 0
			
	pp.append([ouId, tId, postsPerInstructor, postsPerStudent, numInstructors, numStudents, numOps, opPerStudent, first, last, duration])

for p in pp:
	print(p)