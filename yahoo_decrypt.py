'''
Justina Choi
jc8415@nyu.edu
Information Security and Privacy - Cappos
Assignment 1.2
September 19, 2017
Yahoo passwords were stored in plaintext; this script just formats
'''

f = open('yahoo.txt')
results = open('yahoo_results.txt', 'w')

flag = 0
count = 0

for line in f:

    if (line.startswith('4. Final Notes')) and (flag == 1):
        print 'Finished searching'
        break

    if flag == 1:
        line = line.replace('\t', '').replace('\n', '').replace('\r', '')
        text = line.split(':')
        if len(text) != 1:
            # print text
            results.write('%s %s\n' % (text[2], text[2]))
        count += 1

    if line.startswith('user_id   :  user_name  : clear_passwd : passwd'):
        flag = 1
        print 'Starting search from... %s' % line

print 'Found %s emails and passwords' % count
