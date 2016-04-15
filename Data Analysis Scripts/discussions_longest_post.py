from pymongo import MongoClient
import pymongo
import pprint
import json
import csv
import re


client = MongoClient("mongodb://Jamess-MBP.attlocal.net:27017")
db = client.valence
items = db.discuss.find({})

longPostIds = []

cutoff = 2000
num = 0

for item in items:
	pId = item['_id']
	message = item['messageString']
	count = len(re.findall(r'\w+', message))
	
	if count > cutoff:
		# longPostIds.append([pId, count])
		num += 1


print(num)


'''
pId = 954720

items = db.discuss.find({ "_id" : 954720 })

for item in items:
	message = item['messageString']
	count = len(re.findall(r'\w+', message))
	print(count)
'''

print("Complete")