from pymongo import MongoClient
import pymongo
import json
import csv
from mongo_db_connect import db
from scipy.stats.stats import pearsonr
from datetime import datetime

items = db.topics.find({}, no_cursor_timeout=True)

pp = []

for item in items:
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

	ops = db.discuss.find({ 'topicId' : tId, 'parentPostId' : None }, no_cursor_timeout=True)
	numOps = 0
	dates = []

	for op in ops:
		numOps += 1
		datePosted = op['datePosted']
		dates.append(datePosted)
		ouId = op['d2lid']

	first = min(dates)
	last = max(dates)
	d1 = datetime.strptime(first[0:10], "%Y-%m-%d")
	d2 = datetime.strptime(last[0:10], "%Y-%m-%d")
	duration = abs((d2 - d1).days)

	if numStudents > 0:
		opPerStudent = float(numOps) / float(numStudents)
	else:
		opPerStudent = 0



	if classification == 'Academic':
		pp.append([ouId, tId, postsPerInstructor, postsPerStudent, numInstructors, numStudents, numOps, opPerStudent, first, last, duration])


for p in pp:
	print(p)

