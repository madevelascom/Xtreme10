__author__ = 'madevelasco'

import fileinput

def main():
	carbon, hydrogen, oxygen = 0, 0, 0
	for line in fileinput.input():
		line = str(line)
		(line).strip()
		first = line.split()
		carbon, hydrogen, oxygen = int(first[0]), int(first[1]), int(first[2])


if __name__ == '__main__':
	main()