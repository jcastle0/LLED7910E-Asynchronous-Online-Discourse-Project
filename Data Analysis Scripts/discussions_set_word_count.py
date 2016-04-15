from pymongo import MongoClient
from HTMLParser import HTMLParser
import pymongo
import json
import csv
import re


client = MongoClient("mongodb://Jamess-MBP.attlocal.net:27017")
db = client.valence

parser = HTMLParser()

items = db.discuss.find({})

for item in items:

	pId = item['_id']
	message = item['messageFinal']

	count = len(re.findall(r'\w+', message))
	post = db.discuss.update_one(
		{ "_id" : pId }, 
		{
			"$set" : {
				"wordCount" : count
			},
		}, upsert = False
	)