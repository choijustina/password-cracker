'''
Justina Choi
jc8415@nyu.edu
Information Security and Privacy - Cappos
Assignment 1.2
September 21, 2017
'''

import datetime
import hashlib

def hash(password):
	return hashlib.sha256(password).hexdigest()

def salt():
	vals = []
	for num in range(0, 100):
		if num < 10:
			vals.append('0' + str(num))
		else:
			vals.append(str(num))
	return vals

data = open('formspring.txt')
testpw = open('rockyou.txt')
results = open('formspring_results.txt', 'w')

count = 0
success = 0

print 'May the odds be ever in your favor... %s' % (datetime.datetime.now())

dataSet = set()
for d in data:
	dataSet.add(d.replace('\n', ''))

for pw in testpw:
	pw = pw.replace('\n', '')
	for s in salt():
		hashed = hash(pw + s)
		if hashed in dataSet:
			results.write('%s %s\n' % (hashed, pw))
			print '%s %s' % (hashed, s)
			success += 1
			if success > 1000:
				break
		count += 1
		if count % 10000000 == 0:
			print 'Tried %s hashes... %s' % (count, datetime.datetime.now())

data.close()
testpw.close()
results.close()

print '%s cracked!' % success
print 'Finished %s hashes and wrote results to formspring_results.txt' % count
print 'End time: %s' % (datetime.datetime.now())
