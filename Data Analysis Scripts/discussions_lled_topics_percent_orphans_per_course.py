from pymongo import MongoClient
import pymongo
import json
import csv
from mongo_db_connect import db

items = db.topics.find({ 'lled' : True })

courseDict = {}

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
		numThreads = item['numThreads']
		firstPostDatetime = item['firstPostDatetime']
		lastPostDateTime = item['lastPostDateTime']
		topicDurationInDays = item['topicDurationInDays']
		ouId = item['ouId']
		numberOfOpPerStudent = item['numberOfOpPerStudent']
		courseName = item['courseName']
		shortCourseName = item['shortCourseName']
		orphanOp = item['orphanOp']
		nonOrphanOp = item['nonOrphanOp']
		totalOp = item['totalOp']
		percentOrphan = item['percentOrphan']

		if courseName not in courseDict:
			courseDict.update( { courseName : { 'totalOp' : 0,  'orphanOp' : 0, 'totalTopics' : 0, 'ouId' : ouId } } )

		courseDict[courseName]['totalOp'] += totalOp
		courseDict[courseName]['orphanOp'] += orphanOp
		courseDict[courseName]['totalTopics'] += 1

print("Course Name" + ", " + "Total OP" + ", " + "Orphan OP" + ", " + "Total Topics" + ", " + "Percent Orphans" + ", " + "OU ID")

for c in courseDict:
	name = c
	counts = courseDict[c]
	t = counts['totalOp']
	o = counts['orphanOp']
	tt = counts['totalTopics']
	ouId = counts['ouId']
	p = (float(o) / float(t)) * 100
	formattedCoursePercent = name + ": " + ('%.2f' % p) + "%"
	print( name + ", " + str(t) + ", " + str(o) + ", " + str(tt) + ", " + str(p) + ", " + str(ouId))

	# print( formattedCoursePercent + " | " + "Total topics: " + str(tt) + " | " + "Total OP: " + str(t))