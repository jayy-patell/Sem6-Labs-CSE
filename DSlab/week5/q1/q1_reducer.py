#!/usr/bin/env python
"""reducer.py"""
from operator import itemgetter
import sys
import pandas as pd
current_word = None
current_count = 0


# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# parse the input we got from mapper.py
	word, count = line.split('\t', 1)

	# convert count (currently a string) to int
	try:
		count = int(count)
	except ValueError:
		continue

	# this IF-switch only works because Hadoop sorts map output
	# by key (here: word) before it is passed to the reducer
	if current_word == word:
		current_count += count
	else:
		if current_word:
		# write result to STDOUT
			print ('%s\t%s' % (current_word, current_count))
		current_count = count
		current_word = word

# do not forget to output the last word if needed!
if current_word == word:
	print ('%s\t%s' % (current_word, current_count))



# to run: python3 q1_mapper.py| sort |python3 q1_reducer.py > out.txt