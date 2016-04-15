from pymongo import MongoClient
import pymongo
import json
import csv
from mongo_db_connect import db

items = db.discuss.find({})

for item in items:
	
	# Post Variables
	pId = item['_id'] # Post ID, also unique key in mongo
	replyPostIds = item['replyPostIds']
	parentPostId = item['parentPostId']

	if parentPostId == None:
		db.originalPosts.insert_one( {
			'_id' : pId,
			})