from pymongo import MongoClient
from datetime import datetime
import pymongo
import json
import requests
import auth as d2lauth
from auth import *
import time 

startTime = datetime.now()

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

client = MongoClient("mongodb://s172-20-144-h236.paws.uga.edu:27017")
db = client.valence
courseCollection = db.courses
contentCollection = db.content
discussionCollection = db.discuss

# Find all original posts
originalPosts = discussionCollection.find({'parentPostId' : None}, no_cursor_timeout=True)

opNum = 0
replyOneNum = 0
transacNum = 0

for op in originalPosts:
	opId = op['postId']
	opuId = op['postingUserId']
	opNum += 1


	
	replyOnePosts = discussionCollection.find({'parentPostId' : opId}, no_cursor_timeout=True)

	for rOnePost in replyOnePosts:
		rOnePostId = rOnePost['postId']
		rOnePoster = rOnePost['postingUserId']
		replyOneNum += 1
		'''
		transacPosts = discussionCollection.find({'parentPostId' : rOnePostId, 'postingUserId' : opuId}, no_cursor_timeout=True)

		for tp in transacPosts:
			transacNum += 1
			print(tp['postId'])
	'''

print("Original Posts: " + str(opNum))
print("R One Posts: " + str(replyOneNum))
'''
print("Transactions: " + str(transacNum))
print("Complete")
'''
print(datetime.now() - startTime)

