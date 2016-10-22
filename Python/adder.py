__author__ = 'madevelasco'

import fileinput

def transform(a, base, base_map):
	count = 0
	num = 0
	for i in reversed(a):
		num = (base_map.index(i))*(base)**count+num
		count+=1
	return num

def detransform(b, base, base_map):
	count = 0
	num = ''
	while b >1:
		num = num + str((b % base)*(b**count))
		b = b // base
	return num

def main():
	first, second, third = True, True, True
	base = 0
	base_map = []
	num1, num2 = 0, 0


	for line in fileinput.input():
		line = str(line)
		line = line.strip() 
		if(first):
			res = line.split()
			base = int(res[0])
			base_map = res[1]
			first = False
		elif(second):
			num1 = line
			second = False
		else:
			num2 = line[1:]
			without = transform(num1, base, base_map) + transform(num2, base, base_map)
			print(detransform(without, base, base_map))


if __name__ == '__main__':
	main()