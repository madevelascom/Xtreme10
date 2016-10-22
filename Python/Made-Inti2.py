__author__ = 'madevelasco'

import fileinput


def gGDCcd(a,b):
	if b > a:
		return gGDCcd(b, a)
	if a % b == 0:
		return b
	return gGDCcd(b, a % b)

def sum(alist):
    x= 0
    for i in alist:
        x = x + int(i)
    return x

def main():
	first = True
	aset = 0
	for line in fileinput.input():
		if (first):
			first = False
		else:
			line = str(line)
			res = line.strip
			res = line.split(' ')
			inti = int(res [0])
			lower = int(res[1])
			upper = int(res[2])
			for test in range (lower, upper+1, 1):
				if (gGDCcd(test, inti) == 1):
					aset = aset + test
			print(aset)
			aset = 0

if __name__ == '__main__':
	main()