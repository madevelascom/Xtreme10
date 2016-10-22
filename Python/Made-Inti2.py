__author__ = 'madevelasco'

import fileinput


def gGDCcd(x,y):
	if b > a:
        return gcd(b, a)
    if a % b == 0:
        return b
    return gcd(b, a % b)

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
			res = [int(i) for i in res]
			inti = res [0]
			lower = res[1]
			upper = res[2]
			for test in range (lower, upper+1, 1):
				if (gGDCcd(test, inti) == 1):
					aset = aset + test
			print(aset)
			aset = 0

if __name__ == '__main__':
	main()