from pymongo import MongoClient
import pymongo
import json
import csv


client = MongoClient("mongodb://Jamess-MBP.attlocal.net:27017")
db = client.valence
items = db.discuss.find({})

courseList = []

for item in items:
	course = item['courseName']

	if course not in courseList:
		courseList.append(course)


for c in courseList:
	coursePosts = db.discuss.find({ 'courseName' : c })
	studentPosts = 0
	instructorPosts = 0
	taPosts = 0
	totalPosts = 0

	for p in coursePosts:

		pId = p['_id']
		user = p['postingUserId']
		role = p['role']

		totalPosts += 1

		if role == "Student":
			studentPosts += 1

		if role == "Instructor":
			instructorPosts += 1

		if role == "Teaching Assistant" or role == "TA - Designer" or role == "TA - Grader":
			taPosts += 1

	studentPercent = 100 * (float(studentPosts) / float(totalPosts))
	print(c)
	print("%.2f" % round(studentPercent,2) + "%")