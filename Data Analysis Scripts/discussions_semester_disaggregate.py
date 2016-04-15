from pymongo import MongoClient
import pymongo
import json
import csv


client = MongoClient("mongodb://Jamess-MBP.attlocal.net:27017")
db = client.valence
items = db.discuss.find({})
semesterList = []
semesterDict = {}

for item in items:

	semester = item['semester']
	if semester not in semesterList:
		semesterList.append(semester)

for semester in semesterList:

	semesterItems = db.discuss.find( { 'semester' : semester} )
	courseList, studentList, instructorList = [], [], []

	for s in semesterItems:

		pId = s['_id']
		role = s['role']
		course = s['courseName']
		userId = s['postingUserId']

		if semester not in semesterDict:
			semesterDict.update( {semester : 
				{

				"posts" : 0,
				"courses" : 0,
				"students" : 0,
				"instructors" : 0

				}
			})

		semesterDict[semester]["posts"] += 1

		if course not in courseList:
			semesterDict[semester]["courses"] += 1
			courseList.append(course)

		if role == "Student" and userId not in studentList:
			semesterDict[semester]["students"] += 1
			studentList.append(userId)

		if role == "Instructor" and userId not in instructorList:
			semesterDict[semester]["instructors"] += 1
			instructorList.append(userId)

for sem in semesterDict:
	print(sem)
	print(semesterDict[sem])
