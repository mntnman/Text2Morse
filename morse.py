#!/usr/bin/python

import sys, traceback

myFile = '/Users/phooper/dev/python/morseCharMap.txt'
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

#for x in morseMap.keys():
	#print "key = %s and value is %s." % (x,morseMap[x])

while True:
	c = sys.stdin.read(1)
	if c == ' ':
	  sys.stdout.write('/')
	  sys.stdout.flush()
	  continue

	if c == '\n':
	  print
	  continue

	c = c.upper()
	sys.stdout.write(morseMap[c])
	sys.stdout.flush()
