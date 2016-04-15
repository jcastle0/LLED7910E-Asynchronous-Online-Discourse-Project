from pymongo import MongoClient
from HTMLParser import HTMLParser
import pymongo
import json
import csv
import re


client = MongoClient("mongodb://Jamess-MBP.attlocal.net:27017")
db = client.valence

items = db.discuss.find({})

for item in items:

	pId = item['_id']
	role = item['role']
	message = item['messageFinal']
	semester = item['semester']
	course = item['courseName']
	topic = item['topicId']

	print(role)