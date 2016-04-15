from pymongo import MongoClient
from HTMLParser import HTMLParser
import pymongo
import json
import csv


client = MongoClient("mongodb://Jamess-MBP.attlocal.net:27017")
db = client.valence

parser = HTMLParser()

items = db.discuss.find({})
countDict = {
	"messageClean" : 0,
	"messageFinal" : 0,
	"messageNoReply" : 0,
	"messageString" : 0,
	"message" : 0
}

for item in items:

	pId = item['_id']

	try:
		messageFinal = item['messageFinal']
		countDict['messageFinal'] += 1

	except:

		try: 
			messageClean = item['messageClean']
			message = messageClean
			countDict['messageClean'] += 1

		except:
		
			try:
				messageNoReply = item['messageNoReply']
				message = messageNoReply
				countDict['messageNoReply'] += 1

			except:

				messageString = item['messageString']
				message = messageString
				countDict['messageString'] += 1

print(countDict)
'''
messageFinal = parser.unescape(message)

post = db.discuss.update_one(
	{ "_id" : pId }, 
	{
		"$set" : {
			"messageFinal" : messageFinal
		},
	}, upsert = False
)
'''