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

roleDict = {
	"195" : "Instructor",
	"196" : "Student",
	"Error" : "Error",
	"494" : "Teaching Assistant",
	"495" : "TA - Designer",
	"471" : "Collaborative Admin",
	"351" : "Demo Student",
	"496" : "TA - Grader",
	"194" : "Institutional Admin",
	"413" : "No Role",
	"411" : "Student Auditor"
}

roles = []

for item in items:

	pId = item['_id']
	role = str(item['userRole'])
	message = item['messageFinal']
	semester = item['semester']
	course = item['courseName']
	topic = item['topicId']

	post = db.discuss.update_one(
		{ "_id" : pId }, 
		{
			"$set" : {
				"role" : roleDict[role]
			},
		}, upsert = False
	)