from pymongo import MongoClient
import pymongo
import json
import csv
from mongo_db_connect import db

courses = db.discussCourses.find({})

def queryReplyIds(pId):
	fullPostData = db.discuss.find( { "_id" : pId } )
	replyIds = fullPostData[0]['replyPostIds']
	return replyIds


for course in courses:
	# Descriptive Data
	ouId = course['_id']
	courseName = course['courseName']
	semester = course['semester']

	# Number of Participants
	numParticipants = course['participantCount']
	numStudents = numParticipants['students']
	numInstructors = numParticipants['instructors']
	numTeachingAssistants = numParticipants['teachingAssistants']

	# Number of Posts
	postCounts = course['postCounts']
	totalPostCount = postCounts['total']
	studentPostCount = postCounts['students']
	instructorPostCount = postCounts['instructors']
	teachingAssistantPostCount = postCounts['teachingAssistants']

	# Number of Original Posts
	originalPostCounts = course['originalPostCounts']
	totalOriginalPostCount = originalPostCounts['total']
	studentOriginalPostCount = originalPostCounts['students']
	instructorOriginalPostCount = originalPostCounts['instructors']
	teachingAssistantOriginalPostCount = originalPostCounts['teachingAssistants']

	# Original Post IDs
	originalPostIds = course['originalPostIds']
	allOriginalPostIds = originalPostIds['total']
	studentOriginalPostIds = originalPostIds['students']
	instructorOriginalPostIds = originalPostIds['instructors']
	teachingAssistantOriginalPostIds = originalPostIds['teachingAssistants']

	for op in studentOriginalPostIds:
		

