from pymongo import MongoClient
import pymongo
import json
import csv
from mongo_db_connect import db

items = db.topics.find({ 'lled' : True })

semesterSet = set()
topicDict = {}
courseDict = {}

for item in items:
	semester = item['semester']
	semesterSet.add(semester)
	topicDict.update({ semester : 0 })
	courseDict.update({ semester : 0 })

for s in semesterSet:
	cTopics = db.topics.find({ 'lled' : True, 'semester' : s })
	courseSet = set()

	for c in cTopics:
		courseName = c['shortCourseName']
		courseSet.add(courseName)
		topicDict[s] += 1

	for n in courseSet:
		courseDict[s] += 1

print(topicDict)
print(courseDict)