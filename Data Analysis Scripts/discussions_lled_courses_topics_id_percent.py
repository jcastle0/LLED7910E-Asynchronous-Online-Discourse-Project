from pymongo import MongoClient
import pymongo
import json
import csv
from mongo_db_connect import db
from datetime import datetime
import pprint

start = datetime.now()

pp = pprint.PrettyPrinter(indent=4)

items = db.PostsPerCourse.find({})

for item in items:
		courseName = item['_id']
		idTopics = item['numTopics']
		topicSet = set()

		topics = db.discuss.find( { 'courseName' : courseName } )
		for t in topics:
			topicName = t['topicId']
			topicSet.add(topicName)

		totalTopics = len(topicSet)
		percent = float(idTopics) / float(totalTopics)
		
		db.PostsPerCourse.update_one ( 
			{ '_id' : courseName },
			{
				'$set' : { 'totalCourseTopics' : totalTopics, 'percentCourseTopicsUsed' : percent }
			}, upsert=False
			)

print(datetime.now() - start)