from pymongo import MongoClient
import pymongo
import pprint
import json
import requests
import auth as d2lauth
from auth import *
import csv
import re

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

userId = 326261

items = db.discuss.find({ 'postingUserId' : userId })

count = 0

for item in items:
	pId = item['_id']
	userId = str(item['postingUserId'])
	ouId = str(item['d2lid'])
	userRole = str(item['userRole'])
	courseName = item['courseName']
	message = item['messageString']
	print(message)
	count = len(re.findall(r'\w+', message))
	print(count)

print("Complete")