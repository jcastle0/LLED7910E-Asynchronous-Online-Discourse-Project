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

		nonOrphanOp = 0
		orphanOp = 0

		posts = db.discuss.find({ 'topicId' : tId}, no_cursor_timeout=True)

		for p in posts:
			parentPostId = p['parentPostId']
			replyPostIds = p['replyPostIds']

			if parentPostId == None and len(replyPostIds) == 0:
				orphanOp += 1
			elif parentPostId == None:
				nonOrphanOp += 1

		totalOp = orphanOp + nonOrphanOp

		percentOrphan = float(orphanOp) / float(totalOp)

		db.topics.update_one( 
			{ '_id' : tId },
			{
				'$set' : { 
							'orphanOp' : orphanOp,
							'nonOrphanOp' : nonOrphanOp,
							'totalOp' : totalOp,
							'percentOrphan' : percentOrphan
						}
			}, upsert=False
			)