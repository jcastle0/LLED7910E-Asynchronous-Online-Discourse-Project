from pymongo import MongoClient
import pymongo
import json
import csv
from mongo_db_connect import db
from scipy.stats.stats import pearsonr

items = db.topics.find({})

ppsA = []
ppiA = []
ppA = []

ppsI = []
ppiI = []

ppsH = []
ppiH = []

c = set()

for item in items:
	tId = item['_id']
	topicName = item['topicName']
	topicDescription = item['topicDescription']
	semester = item['semester']
	classification = item['classification']
	totalPosts = item['TotalPosts']
	numStudents = item['NumUniqueStudents']
	numInstructors = item['NumUniqueInstructors']
	numTas = item['NumUniqueTas']
	numStudentPosts = item['NumStudentPosts']
	numInstructorPosts = item['NumInstructorPosts']
	numTaPosts = item['NumTaPosts']
	postsPerStudent = item['postsPerStudent']
	postsPerInstructor = item['postsPerInstructor']

	c.add(classification)

	if classification == 'Academic':
		ppsA.append(postsPerStudent)
		ppiA.append(postsPerInstructor)
		ppA.append([tId, postsPerInstructor, postsPerStudent, numInstructors, numStudents])

	if classification == 'Introductions':
		ppsI.append(postsPerStudent)
		ppiI.append(postsPerInstructor)

	if classification == 'Help':
		ppsH.append(postsPerStudent)
		ppiH.append(postsPerInstructor)

correlA = pearsonr(ppsA, ppiA)
correlI = pearsonr(ppsI, ppiI)
correlH = pearsonr(ppsH, ppiH)

for p in ppA:
	print(str(p[0]) + ", " + str(p[1]) + ", " + str(p[2]) + ", " + str(p[3]) + ", " + str(p[4]))