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

	posts = db.discuss.find({ 'topicId' : tId })

	studentPosts = 0
	instructorPosts = 0
	taPosts = 0
	totalPosts = 0
	studentSet = set()
	instructorSet = set()
	taSet = set()

	for p in posts:
		role = p['role']
		userId = str(p['userIdEncrypt'])
		totalPosts += 1

		if role == 'Student':
			studentPosts += 1
			studentSet.add(userId)

		elif role == 'Instructor':
			instructorPosts += 1
			instructorSet.add(userId)

		elif role == 'Teaching Assistant' or role == 'TA - Grader' or role == 'TA - Designer':
			taPosts += 1
			taSet.add(userId)

	uniqueStudents = len(studentSet)
	uniqueInstructors = len(instructorSet)
	uniqueTas = len(taSet)

	db.topics.update_one(
		{ '_id' : tId },
		{
			'$set' : { 
				'NumStudentPosts' : studentPosts,
				'NumInstructorPosts' : instructorPosts,
				'NumTaPosts' : taPosts,
				'TotalPosts' : totalPosts,
				'NumUniqueStudents' : uniqueStudents,
				'NumUniqueInstructors' : uniqueInstructors,
				'NumUniqueTas' : uniqueTas
			}
		}, upsert=False
		)

	print(tId)
	print("Student Posts: " + str(studentPosts))
	print("Instructor Posts: " + str(instructorPosts))
	print("TA Posts: " + str(taPosts))
	print("Total Posts: " + str(totalPosts))
	print("Total Unique Students: " + str(uniqueStudents))
	print("Total Unique Instructors: " + str(uniqueInstructors))
	print("---------------------------------------------------")
	print("Total Unique TAs:" + str(uniqueTas))