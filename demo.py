import json
import random

file = open("questionset.json")

questionSet = []
tag = []
questionType = {}
questionSet = json.load(file)

def getItem(data):
	index = random.randint(1, len(data))
	return index

def getLength(data):
	return len(data)

def getType(data):
	# 1: MC
	# 3: Plain Text
	# 10: Programming Question
	type = {
		"1": 0,
		"3": 0,
		"10": 0,
	}
	for i in range(0,len(data)):
		if data[i]["type"] == "1":
			type["1"] = type["1"] + 1
			
		elif data[i]["type"] == "3":
			type["3"] = type["3"] + 1
		elif data[i]["type"] == "10":
			type["10"] = type["10"] + 1
		else:
			print "?",data[i]
	return type

def getTag(data):
	t = []
	for i in range(0,len(data)):
		if data[i].has_key("tag"): 
			if data[i]["tag"]!= "":
				if len(t) == 0:
					t.append(data[i]["tag"])
				elif data[i]["tag"] not in t:
					t.append(data[i]["tag"])				
	return t
	

#get question set array
print "The number of questions:", getLength(questionSet)

print ""

print "get a question randomly:"
print questionSet[getItem(questionSet)]

print ""

questionType = getType(questionSet) 
print "Question Type Distribution:"
print "Multiple Choice Question:", questionType["1"]
print "Plain text Question:", questionType["3"]
print "Programming Question:", questionType["10"]

print ""

tag = getTag(questionSet)
print "Question Tag:"
for i in range(0,len(tag)):
	print tag[i]