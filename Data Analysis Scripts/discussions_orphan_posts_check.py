from pymongo import MongoClient
import pymongo
import json
import csv
from mongo_db_connect import db

items = db.orphan.find({})
count = 0

for item in items:
	count += 1

print(count)