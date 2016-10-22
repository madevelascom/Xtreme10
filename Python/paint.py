__author__ = 'madevelasco'

import fileinput
import itertools
from collections import Counter

def sol(color_sequence):
	histogram = Counter(color_sequence)
	i, prev = 0,
	first_brush, sec_brush = 0, 0

	for x in color_sequence:
		if (x == prev):
			first_brush = x
			histogram[x] = histogram[x]-1
		else:
			if(histogram[x] != 0):
				sec_brush = x
				prev = x
			else:
				first_brush = x
				prev = x

def main():
	scenarios = True
	numcolors = True
	squence = True
	varietycolor = 0
	color_sequence = []
	
	for line in fileinput.input():		
		line = str(line)
		(line).strip()
		if (scenarios):
			scenarios = False
		elif(numcolors):
			varietycolor = int(line)
			numcolors = False
		elif(squence):
			color_sequence = line.split()


if __name__ == '__main__':
	main()
