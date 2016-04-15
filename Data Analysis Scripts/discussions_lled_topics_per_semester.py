from pymongo import MongoClient
import pymongo
import json
import csv
import pprint
from mongo_db_connect import db
from datetime import datetime
import time

startTime = datetime.now()

pp = pprint.PrettyPrinter(indent=4)

items = db.topics.find({ 'lled' : True }, no_cursor_timeout=True)
semesterDict = {}
count = 0


for item in items:
		count += 1
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

		if semester not in semesterDict:
			semesterDict.update( { semester : { 'topicCount' : 0, 'orphans' : 0, 'studentPosts' : 0, 'instructorPosts' : 0, 'taPosts' : 0, 'postCount' : 0 } } )
		
		semesterDict[semester]['topicCount'] += 1
		semesterDict[semester]['studentPosts'] += numStudentPosts
		semesterDict[semester]['instructorPosts'] += numInstructorPosts
		semesterDict[semester]['taPosts'] += numTaPosts
		semesterDict[semester]['orphans'] += orphanOp

		posts = db.discuss.find({ 'topicId' : tId }, no_cursor_timeout=True)

		for p in posts:
			semesterDict[semester]['postCount'] += 1

print(count)

for s in semesterDict:
	print(str(s) + ", " + str(semesterDict[s]['topicCount']) + ", " + str(semesterDict[s]['postCount']))


print(datetime.now() - startTime)