from pymongo import MongoClient
import pymongo
from HTMLParser import HTMLParser
import json
import csv
from mongo_db_connect import db

items = db.discuss.find({})

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

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
	topicDescription = item['topicDescription']
	threadId = item['threadId']

	s = MLStripper()
	s.feed(topicDescription)
	topicDescriptionClean = s.get_data()

	post = db.discuss.update_one(
		{ "_id" : pId }, 
		{
			"$set" : {
				"topicDescriptionClean" : topicDescriptionClean
			},
		}, upsert = False
	)