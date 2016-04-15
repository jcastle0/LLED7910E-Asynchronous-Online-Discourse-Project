from pymongo import MongoClient
import pymongo
import json
import csv
from mongo_db_connect import db

courses = db.discussCourses.find({})

for course in courses:
	ouId = course['_id']

	items = db.discuss.find({ 'd2lid' : ouId })
	students = set()
	instructors = set()
	tas = set()

	studentList = []
	instructorList = []
	taList = []

	for item in items:
		
		# User Variables
		userId = str(item['userIdEncrypt'])
		userRole = str(item['userRole']) # D2L User Code
		role = item['role'] # Human Readable Role

		if role == 'Student':
			students.add(userId)

		if role == 'Instructor':
			instructors.add(userId)

		if role == 'Teaching Assistant' or role == 'TA - Designer' or role == 'TA - Grader':
			tas.add(userId)


	for s in students:
		studentList.append(s)

	for i in instructors:
		instructorList.append(i)

	for t in tas:
		taList.append(t)
		
	db.discussCourses.update_one(
		{ '_id' : ouId },
		{
			'$set' : {
				"participants.students" : studentList,
				"participants.instructors" : instructorList,
				"participants.teachingAssistants" : taList
			},
		}, upsert=False
	)