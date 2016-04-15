from pymongo import MongoClient
import pymongo
import json
import csv
from mongo_db_connect import db

items = db.discuss.find({})
totalCount = 0
roleCount = {}
courseCount = set()

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
	
	# Discussion Variables
	forumId = item['forumId']
	forumName = item['forumName']
	topicId = item['topicId']
	topicName = item['topicName']
	topicDescription = item['topicDescriptionClean']
	threadId = item['threadId']

	totalCount += 1

	if role in roleCount:
		roleCount[role] += 1
	else:
		roleCount.update({ role : 0 })

	courseCount.add(courseName)

print(totalCount)
print(roleCount)
print(len(courseCount))