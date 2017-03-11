#!/usr/bin/python

import sys, traceback

myFile = 'morseCharMap.txt'
morseMap = {}

## Open the map file if we can >:/
try:
	f = open(myFile)
except IOError:
	print "Open map file failed"
	sys.exit(1)

## Read the first line 
line = f.readline()

#------------  Load the hash table with the char-to-morse ------------
while line:
    line = line.rstrip('\n')
    list = line.split("|")
    morseMap[list[0]] = list[1]
    # print "%s is equal to %s" % (list[0],list[1])
    list = ""
    line = f.readline()

f.close()

for c in sys.stdin:
	continue

#for x in morseMap.keys():
#	print "key = %s and value is %s." % (x,morseMap[x])

c = c.upper()
c = c.replace(" ", "")
c = c.rstrip()
for x in c:
	print morseMap[x] + " ",

sys.exit(0)
