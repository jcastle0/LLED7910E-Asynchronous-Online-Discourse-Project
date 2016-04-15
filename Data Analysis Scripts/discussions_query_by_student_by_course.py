from pymongo import MongoClient
import pymongo
import pprint
import json
import requests
import auth as d2lauth
from auth import *
import csv

with open('cred/cred-dev.json') as cred_file:
	cred = json.load(cred_file)

app_id = cred["appID"]
app_key = cred["appKey"]
redirect_url_attributes = cred["redirectUrlAttributes"]
base_url = cred["url"]
app_creds = { 'app_id': app_id, 'app_key': app_key }
redirect_url_base = "https://" + base_url + "/d2l/home"
ac = d2lauth.fashion_app_context(app_id=app_creds['app_id'], app_key=app_creds['app_key'])
auth_url = ac.create_url_for_authentication(base_url, 'http://127.0.0.1:8000')
redirect_url = redirect_url_base + redirect_url_attributes
uc = ac.create_user_context(redirect_url, base_url, True)


client = MongoClient("mongodb://s172-21-129-h45.paws.uga.edu:27017")
db = client.valence

items = db.discuss.find({})

myDict = {}
myList = []

for item in items:
	pId = item['_id']
	userId = str(item['postingUserId'])
	ouId = str(item['d2lid'])
	userRole = str(item['userRole'])
	courseName = item['courseName']

	unique = userId + courseName

	if userRole == '196':

		if unique not in myList:
			myList.append(unique)

			if courseName not in myDict:
				myDict.update({courseName: 0})

			
			myDict[courseName] += 1

writer = csv.writer(open('posts_by_unique_students_per_course.csv', 'w'))
for key, value in myDict.items():
	writer.writerow([key, value])

'''
with open('results.csv', 'w') as resultFile:
	fieldNames = ['Course', 'Number of Posts']
	writer = csv.DictWriter(resultFile, myDict.keys())
	writer.writeheader()
	writer.writerow(myDict)
'''

print("Complete")