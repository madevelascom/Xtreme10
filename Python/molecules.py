__author__ = 'madevelasco'

import fileinput
import itertools

def lowest(a, b, c):
	return sorted([a,b,c])[0] 

def cal_glucose(carbon, hydrogen, oxygen):
	cal_1 = carbon//6
	cal_2 = hydrogen//12
	cal_3 = oxygen//6
	return lowest(cal_1, cal_2, cal_3)

def cal_water(carbon, hydrogen, oxygen):
	cal_1 = oxygen+hydrogen
	cal_2 = hydrogen//2
	cal_3 = oxygen//1
	return lowest(cal_1, cal_2, cal_3)

def cal_carbon(carbon, hydrogen, oxygen):
	cal_1 = carbon//1
	cal_2 = carbon+oxygen
	cal_3 = oxygen//2
	return lowest(cal_1, cal_2, cal_3)

def main():
	#C6H12O6 GLUCOSE
	#H20 WATER
	#CO2 CARBON DIOXIDE
	carbon, hydrogen, oxygen = 0, 0, 0
	ult_wat, ult_diox, ult_carb = 0, 0, 0
	max = 0

	for line in fileinput.input():
		line = str(line)
		(line).strip()
		first = line.split()
		carbon, hydrogen, oxygen = int(first[0]), int(first[1]), int(first[2])

	ordering = itertools.permutations([1,2,3])
	for x in ordering:
		max_glucose, max_water, max_carbon = 0, 0, 0
		carbon, hydrogen, oxygen = int(first[0]), int(first[1]), int(first[2])
		for perm in x:
			if (perm == 1):
				max_glucose = cal_glucose  (carbon, hydrogen, oxygen)
				carbon, hydrogen, oxygen = carbon-6*max_glucose, hydrogen-12*max_glucose, oxygen-6*max_glucose
			elif (perm == 2):
				max_water = cal_water (carbon, hydrogen, oxygen)
				carbon, hydrogen, oxygen = carbon-0*max_water, hydrogen-2*max_water, oxygen-1*max_water
			elif(perm==3):
				max_carbon = cal_carbon(carbon, hydrogen, oxygen)
				carbon, hydrogen, oxygen = carbon-1*max_carbon, hydrogen-0*max_carbon, oxygen-2*max_carbon

		if (carbon == 0 and oxygen == 0 and hydrogen ==0):
			val = max_carbon + max_water + max_glucose
			if (val > max):
				max = val
				ult_wat, ult_diox, ult_carb = max_water,  max_carbon, max_glucose
		
	
	if (max == 0): 
		print('Error')
	else:
		print(ult_wat, ult_diox, ult_carb)

if __name__ == '__main__':
	main()