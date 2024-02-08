#!/usr/bin/env python
"""mapper.py"""
import sys
import pandas as pd

df = pd.read_csv('../covid_19_data (1).csv')
words = df['Country/Region']

# increase counters
for word in words:
	# write the results to STDOUT (standard output);
	# what we output here will be the input for the
	# Reduce step, i.e. the input for reducer.py
	#
	# tab-delimited; the trivial word count is 1
	print ('%s\t%s' % (word, 1))


# to run: python3 q1_mapper.py > map.txt