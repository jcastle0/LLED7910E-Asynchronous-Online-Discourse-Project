from pymongo import MongoClient
import pymongo
import json
import csv
from mongo_db_connect import db

items = db.topics.find({ 'lled' : True })

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

		if numTas > 0:
			postsPerTa = float(numTaPosts) / float(numTas)
		else:
			postsPerTa = 0

		print(str(ouId) + "|" + str(tId) + "|" + str(postsPerStudent) + "|" + str(postsPerInstructor) + "|" + str(postsPerTa) + "|" + str(numStudents) + "|" + str(numInstructors) + "|" + str(numTas) + "|" + str(numThreads) + "|" + str(numberOfOpPerStudent) + "|" + str(firstPostDatetime) + "|" + str(lastPostDateTime) + "|" + str(topicDurationInDays))