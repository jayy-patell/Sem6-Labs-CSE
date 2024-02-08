#!/usr/bin/env python
"""mapper.py"""
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()

# split the line into words
words = line.split()

# increase counters
for word in words:
	# write the results to STDOUT (standard output);
	# what we output here will be the input for the
	# Reduce step, i.e. the input for reducer.py
	#
	# tab-delimited; the trivial word count is 1
	print ('%s\t%s' % (word, 1))


# to run: echo "a a a a v v f f hh hh fg tg fg gt nnn ccc ddd nnn ddd"|python3 eg1_mapper.py