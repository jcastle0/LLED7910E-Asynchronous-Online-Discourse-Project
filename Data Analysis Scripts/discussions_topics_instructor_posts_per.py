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

	if numInstructors > 0:
		postsPerInstructor = float(numInstructorPosts) / float(numInstructors)
	else:
		postsPerInstructor = 0

	db.topics.update_one(
		{ '_id' : tId },
		{
			'$set' : { 'postsPerInstructor' : postsPerInstructor }
		}, upsert=False
		)