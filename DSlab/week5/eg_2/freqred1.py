#!/usr/bin/env python
# reducer.py
from __future__ import print_function
import sys

lastWord = None
sum = 0

for line in sys.stdin:
	word, count = line.strip().split('\t', 1)
	count = int(count)
	if lastWord==None:
		lastWord = word
		sum = count
		continue
	if word==lastWord:
		sum += count
	else:
		print( "%s\t%d" % ( lastWord, sum ) )
		sum = count
		lastWord = word

# output last word
if lastWord == word:
	print( '%s\t%s' % (lastWord, sum ) )

# to run: echo "foo foo foo labs labs labs quux labs foo bar quux" |python3 freqmap1.py |sort|python3 freqred1.py