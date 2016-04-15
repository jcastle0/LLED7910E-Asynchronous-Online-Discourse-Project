from pymongo import MongoClient
import pymongo
import json
import csv
from mongo_db_connect import db

items = db.discuss.find({})

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

	firstThree = courseName[0:3]

	if firstThree == "XLS":
		level = int(courseName[11:12])
	else:
		level = int(courseName[4:5])

	if level > 5:
		level = "Graduate"
	else:
		level = "Undergraduate"

	post = db.discuss.update_one(
			{ "_id" : pId }, 
			{
				"$set" : {
					"courseLevel" : level
				},
			}, upsert = False
		)

	print(level)