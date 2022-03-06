from datetime import date, time, datetime
import time
import random
ml = ["Happy Father's Day","You are a great dad","I love you"]
dates = []
month31 = ["1", "3", '5', '7', '9', '10', '12']
def say(thing):
		if thing == "XD" :
			print("what now buddy boy")
		elif thing == "/day":
			print(date.day())
		else:
			print(thing)
gg='hihihih'
def randomday(pri,num):
	for i in range(int(num)):
		dates.append(random.randint(-9999,9999))
		month = random.randint(1,12)
		dates.append(month)
		if month in month31:
			dates.append(random.randint(1,31))
		elif month == "2":
			dates.append(random.randint(1,28))
		else:
			dates.append(random.randint(1,30))
		if pri == "yes":
			print("format = [yyyy,mm,dd]")
			print(dates)
			dates.clear()
		else: 
			return dates
class recur(object):
	def day():
		return date.today()
	def time(repeat):
		for i in range(int(repeat)):
			return datetime.now()
	def message(self):
		return random.choice(ml)
	
def givead():
	return "Pro Features for Brilliant Writing With a Grammarly Premium upgrade, you will have access to new checks and features. We’ve highlighted some of the most popular ones below. Writing Style Settings Customizable settings for business, academic, casual, and creative writing. Confidence Boosters Automatically eliminate hedging language to sound clear and confident. Sentence Structure Go deeper than grammar and keep your sentences smooth and easy to read. Plagiarism Checker Make sure your voice is original and identify passages that need citations. Word Choice Suggestions Vocabulary enhancements help you find the perfect word every time."
