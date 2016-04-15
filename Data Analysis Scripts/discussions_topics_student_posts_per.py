from pymongo import MongoClient
import pymongo
import json
import csv
from mongo_db_connect import db

items = db.topics.find({})

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

	if numStudents > 0:
		postsPerStudent = float(numStudentPosts) / float(numStudents)
	else:
		postsPerStudent = 0

	db.topics.update_one(
		{ '_id' : tId },
		{
			'$set' : { 'postsPerStudent' : postsPerStudent }
		}, upsert=False
		)