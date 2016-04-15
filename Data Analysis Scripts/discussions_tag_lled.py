from pymongo import MongoClient
import pymongo
import json
import csv
from mongo_db_connect import db

with open('lled_topics.json') as jsonFile:
	data = json.load(jsonFile)

count = 0

for d in data:

	tId = d['topic']
	numThreads = d['numberOfThreads']
	firstPostDatetime = d['firstPostDatetime']
	lastPostDateTime = d['lastPostDateTime']
	topicDurationInDays = d['topicDurationInDays']
	ouId = d['ou']
	numberOfOpPerStudent = d['numberOfOpPerStudent']



	items = db.topics.update(
		{ '_id' : tId},
		{
		'$set' : {
					'lled' : True,
					'numThreads' : numThreads,
					'firstPostDatetime' : firstPostDatetime,
					'lastPostDateTime' : lastPostDateTime,
					'topicDurationInDays' : topicDurationInDays,
					'ouId' : ouId,
					'numberOfOpPerStudent' : numberOfOpPerStudent
			},
		}, upsert=False
		)