from pymongo import MongoClient
import pymongo
import json
import csv
from mongo_db_connect import db
from datetime import datetime
import pprint
from statistics import stdev, mean

start = datetime.now()

pp = pprint.PrettyPrinter(indent=4)

items = db.PostsPerCourse.find({})
count = 0
totalTopics = 0

for item in items:
		courseName = item['_id']
		numTopics = item['numTopics']
		totalCourseTopics = item['totalCourseTopics']
		percentCourseTopicsUsed = item['percentCourseTopicsUsed']
		percentPosts = item['percentPosts']
		postsPerStudent = item['postsPerStudent']
		studentsHigh = 0
		studentsLow = 0
		studentsAvg = 0

 		if percentCourseTopicsUsed > .749:
	 		count += 1
	 		totalTopics += numTopics
	 		totalPosts = 0
	 		postNumArray = []

	 		for n in postsPerStudent:
	 			postNum = postsPerStudent[n]
	 			postNumArray.append(postNum)	

	 		for p in percentPosts:
	 			userIdEcryptPer = p
	 			percent = percentPosts[p]
	 		
	 		courseMean = mean(postNumArray)
	 		courseStdev = stdev(postNumArray)

	 		for n in postsPerStudent:
	 			userIDEncryptNum = n
	 			postNum = postsPerStudent[n]
	 			deviance = (courseMean - postNum) / courseStdev

	 			if postNum > (courseMean + courseStdev):
	 				studentsHigh += 1
	 			elif postNum < (courseMean - courseStdev):
	 				studentsLow += 1
	 			else:
	 				studentsAvg += 1
		 	print(courseName + "|" + str(studentsHigh) + "|" + str(studentsLow) + "|" + str(studentsAvg))

print("Total Topics Used: " + str(totalTopics))
print("Total Courses Used: " + str(count))
print(datetime.now() - start)