from pymongo import MongoClient
import pymongo
import json
import csv
from mongo_db_connect import db

courses = db.discussCourses.find({})

for c in courses:
	ouId = c['_id']

	numPosts = 0
	numStudentPosts = 0
	numInstructorPosts = 0
	numTaPosts = 0

	numOriginalPosts = 0
	numOriginalStudentPosts = 0
	numOriginalInstructorPosts = 0
	numOriginalTaPosts = 0

	originalPosts = []
	studentOriginalPosts = []
	instructorOriginalPosts = []
	taOriginalPosts = []

	items = db.discuss.find({ 'd2lid' : ouId })

	for item in items:
		
		# User Variables
		userId = str(item['userIdEncrypt'])
		userRole = str(item['userRole']) # D2L User Code
		role = item['role'] # Human Readable Role
		
		# Post Variables
		pId = item['_id'] # Post ID, also unique key in mongo
		subject = item['subject']
		message = item['messageFinal']
		datePosted = item['datePosted']
		replyPostIds = item['replyPostIds']
		parentPostId = item['parentPostId']
		wordCount = item['wordCount']

		# Course Variables
		ouId = str(item['d2lid']) # D2L Course Id
		courseName = item['courseName']
		semester = item['semester']
		courseLevel = item['courseLevel']
		
		# Discussion Variables
		forumId = item['forumId']
		forumName = item['forumName']
		topicId = item['topicId']
		topicName = item['topicName']
		topicDescription = item['topicDescriptionClean']
		threadId = item['threadId']

		numPosts += 1

		if role == 'Student':
			numStudentPosts += 1
			if parentPostId == None:
				numOriginalPosts += 1
				numOriginalStudentPosts += 1
				originalPosts.append(pId)
				studentOriginalPosts.append(pId)

		if role == 'Instructor':
			numInstructorPosts += 1
			if parentPostId == None:
				numOriginalPosts += 1
				numOriginalInstructorPosts += 1
				originalPosts.append(pId)
				instructorOriginalPosts.append(pId)

		if role == 'Teaching Assistant' or role == 'TA - Designer' or role == 'TA - Grader':
			numTaPosts += 1
			if parentPostId == None:
				numOriginalPosts += 1
				numOriginalTaPosts += 1
				originalPosts.append(pId)
				taOriginalPosts.append(pId)

	db.discussCourses.update_one(
		{ '_id' : ouId },
		{
			'$set' : {
				
				"postCounts.total" : numPosts,
				"postCounts.students" : numStudentPosts,
				"postCounts.instructors" : numInstructorPosts,
				"postCounts.teachingAssistants" : numTaPosts,

				"originalPostCounts.total" : numOriginalStudentPosts,
				"originalPostCounts.students" : numOriginalStudentPosts,
				"originalPostCounts.instructors" : numOriginalInstructorPosts,
				"originalPostCounts.teachingAssistants" : numOriginalTaPosts,

				"originalPostIds.total" : originalPosts,
				"originalPostIds.students" : studentOriginalPosts,
				"originalPostIds.instructors" : instructorOriginalPosts,
				"originalPostIds.teachingAssistants" : taOriginalPosts,
			},
		}, upsert=False
	)