from pymongo import MongoClient
import pymongo
import json
import csv
from mongo_db_connect import db

items = db.discussCourses.find({})

for item in items:
	print(item)