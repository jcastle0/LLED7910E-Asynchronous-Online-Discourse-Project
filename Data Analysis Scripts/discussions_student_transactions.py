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

	op = False

	if parentPostId == None and len(replyPostIds) > 0 and role == 'Student':
		op = True
		opUser = userId
	
	if op:
		for r in replyPostIds:
			replyOnes = db.discuss.find({ '_id' : r , 'role' : 'Student' })

			for rOne in replyOnes:
				rOneReplyIds = rOne['replyPostIds']
				rOneMessage = rOne['messageFinal']

				for x in rOneReplyIds:
					replyTwos = db.discuss.find({ '_id' : x , 'userIdEncrypt' : opUser })
					
					for rTwo in replyTwos:
						rTwoMessage = rTwo['messageFinal']

						print('Original Post----------------------------------------------------------')
						print(message)
						print('Reply One--------------------------------------------------------------')
						print(rOneMessage)
						print('Reply Two--------------------------------------------------------------')
						print(rTwoMessage)
						print('///////////////////////////////////////////////////////////////////////')


	
	
	
	
	