'''
Justina Choi
jc8415@nyu.edu
Information Security and Privacy - Cappos
Assignment 1.2
September 19, 2017
'''

import datetime
import hashlib

data = open('linkedin.txt')
testpw = open('rockyou.txt')
results = open('linkedin_results.txt', 'w')

count = 0
success = 0

print 'Let the games begin...%s' % (datetime.datetime.now())

dataSet = set()
for d in data:
	dataSet.add(d.replace('\n', ''))

for pw in testpw:
	pw = pw.replace('\n', '')
	hashed = hashlib.sha1(pw)
	if hashed.hexdigest() in dataSet:
		results.write('%s %s\n' % (hashed.hexdigest(), pw))
		print '%s is a password' % pw
		success += 1
	count += 1

	if count % 1000000 == 0:
		print 'tried %s passwords %s' % (count, datetime.datetime.now())

data.close()
testpw.close()
results.close()

print '%s cracked!' % success
print 'Finished hashing %s passwords and wrote results to linkedin_results.txt' % count
print 'End time %s' % (datetime.datetime.now())
