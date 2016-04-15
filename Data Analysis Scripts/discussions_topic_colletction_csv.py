from pymongo import MongoClient
import pymongo
import json
import csv
from mongo_db_connect import db

items = db.topics.find({})

outFile = open('topicCSV.csv', 'wb')
writer = csv.writer(outFile)

myDict = {}

fieldnames = ['topicId', 'topicName', 'topicDescription', 'semester']

for item in items:
	
	topicId = item['_id']
	topicName = item['topicName'].encode('utf-8').strip()
	topicDescription = item['topicDescription'].encode('utf-8').strip()
	semester = item['semester'].encode('utf-8').strip()

	myDict.update({

		'topicId' : topicId,
		'topicName' : topicName,
		'topicDescription' : topicDescription,
		'semester' : semester

		})

	with open('topicCSV.csv', 'a') as outFile:
		writer = csv.DictWriter(outFile, fieldnames = fieldnames)
		writer.writerow(myDict)
