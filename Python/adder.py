__author__ = 'madevelasco'

import fileinput

def transform(a, base, base_map):
	count = 0
	num = 0
	for i in reversed(a):
		num = (base_map.index(i))*((base)**count)+num
		count+=1
	return num

def detransform(b, base, base_map):
	count = 0
	num = ''
	while b >1:
		num = str(base_map[b % base]) + num
		b = b // base
		count += 1
	return num

def generate_string(quant, char):
	res = ''
	for i in range(0, quant):
		res = res + char
	return res

def main():
	first, second, third = True, True, True
	base = 0
	base_map = []
	num1, num2 = 0, 0
	result = []
	res = ''
	max = 0

	for line in fileinput.input():
		line = str(line)
		if(first):
			line = line.strip('\n')
			result.append(line)
			res = line.split()
			base = int(res[0])
			base_map = res[1]
			first = False
		elif(second):
			line = line.strip('\n')
			result.append(line)
			num1 = line.strip()
			second = False
		elif(third):
			line = line.strip('\n')
			result.append(line)
			num2 = line[1:].strip()
			without = transform(num1, base, base_map) + transform(num2, base, base_map)
			z = detransform(without, base, base_map)
			result.append(z)
			third = False
	a = 0
	for x in result:
		if (a == 0):
			print(x)
			a += 1
		elif (a == 1 or a==2):
			print(x)
			a += 1
			if (len(x)> max):
				max = len(x)
		elif(a ==3):
			a += 1
			print(generate_string(max, "-"))
			spaces = max - len(x)
			print(generate_string(spaces, " ")+x)
			
			

if __name__ == '__main__':
	main()