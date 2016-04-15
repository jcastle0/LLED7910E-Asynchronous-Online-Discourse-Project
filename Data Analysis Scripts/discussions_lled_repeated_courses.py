from pymongo import MongoClient
import pymongo
import json
import csv
from mongo_db_connect import db

items = db.topics.find({ 'lled' : True })

semesterSet = set()
semesterDict = {}

courseList = []

for item in items:
	semester = item['semester']
	semesterSet.add(semester)
	semesterDict.update({ semester : set() })

for s in semesterSet:
	cTopics = db.topics.find({ 'lled' : True, 'semester' : s })

	for c in cTopics:
		courseName = c['shortCourseName']
		semesterDict[s].add(courseName)

for i in semesterDict:
	print(i)
	courses = semesterDict[i]