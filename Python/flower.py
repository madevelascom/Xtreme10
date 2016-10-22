__author__ = 'madevelasco'

import fileinput

def sol(size):
	alist = list(range(1, size+1))
	count = 0
	flag = True
	while (len(alist) > 1):
		if (count == len(alist)):
			count = 0
			alist = list(filter(None, alist))
		else:
			if (flag):
				count += 1
				flag = False
			else:
				alist[count] = ""
				count += 1
				flag = True

	return alist[0]

def main():
	first = True
	for line in fileinput.input():
		line = str(line)
		(line).strip()
		if (first):
			first = False
		else:
			print(sol(int(line)))

if __name__ == '__main__':
	main()