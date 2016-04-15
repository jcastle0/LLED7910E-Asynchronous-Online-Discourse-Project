from pymongo import MongoClient
import pymongo
import json
import csv
from mongo_db_connect import db

items = db.topics.find({ 'lled' : True }, no_cursor_timeout=True)

orphans = {}

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

		if courseName not in orphans:
			orphans.update({ courseName : {}})

		orphans[courseName].update({ tId : 0 })

		posts = db.discuss.find({ 'topicId' : tId}, no_cursor_timeout=True)

		for p in posts:
			orphan = False
			parentPostId = p['parentPostId']
			replyPostIds = p['replyPostIds']

			if parentPostId == None and len(replyPostIds) == 0:
				orphan = True

			if orphan:
				orphans[courseName][tId] += 1

with open('lled_orphans.json', 'w') as fp:
	json.dump(orphans, fp)