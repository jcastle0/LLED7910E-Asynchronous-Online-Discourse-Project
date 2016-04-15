from pymongo import MongoClient
import pymongo
import json
import csv
from mongo_db_connect import db
from datetime import datetime
import pprint

start = datetime.now()

pp = pprint.PrettyPrinter(indent=4)

userIdEncrypt = '28756b827462249ee0d9b5183a8b3f50218c009e324dc3ca782870065a8e10c4'
course = 'SPED2000E - SURVEY SPECIAL EDUC - 14SP-22760'

items = db.discuss.find( { 'userIdEncrypt' : userIdEncrypt, 'courseName' : course } )
count = 0
for item in items:
	pp.pprint(item)
	print("------------------")
	count += 1
print(count)
