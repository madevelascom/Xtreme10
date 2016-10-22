__author__ = 'madevelasco'

import fileinput
import datetime as dt
from math import radians, cos, sin, asin, sqrt
from operator import itemgetter
import itertools

def distance(lon1, lat1, lon2, lat2):
	lat1 = float(lat1)
	lat2 = float(lat2)
	lon1 = float(lon1)
	lon2 = float(lon2)

	lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
	r = 6378.137*2	
	d = r*asin(sqrt(sin((lat1-lat2)/2)**2 + cos(lat1)*cos(lat2)*(sin((lon1-lon2)/2)**2)))
	#d = 2 × r × arcsin (sqrt (sin2((lat1 - lat2)/2) + cos(lat1) × cos(lat2) × sin2((long1 - long2)/2)))
	return d


def get_item(astr):
	str(astr).strip()
	all =  astr.split(',')
	datet, lat, lon, phone = get_date(all[0]), float(all[1]), float(all[2]), int(all[3])
	item = {'Date&Time': datet, 'Latitude':lat, 'Longitude': lon, 'PhoneNumber': phone}
	return item

	
def get_date(intro):
	return int(dt.datetime.strptime(intro, "%m/%d/%Y %H:%M").strftime("%s"))



def main():
	i = 0
	st_lat, st_lon = 0, 0
	dist = 0.0
	alist = []
	dup_cels = []
	clean = []
	for line in fileinput.input():
		line = str(line)
		if (i == 0):
			(line).strip()
			first = line.split(',')
			st_lat, st_lon = first[0].strip(), first[1].strip()
			i = 1
		elif(i == 1):
			dist = float(line.strip())
			i = 2
		elif(i == 2):
			i = 3
		else:
			alist.append(get_item(line))

	alist.sort(key=itemgetter('Date&Time'), reverse=True)
	for item in alist:
		separation = distance(item['Longitude'],item['Latitude'], st_lon, st_lat)
		if (item['PhoneNumber'] not in dup_cels and separation < dist):
			item['distance'] = separation
			dup_cels.append(item['PhoneNumber'])
			clean.append(item)

	clean.sort(key=itemgetter('PhoneNumber'), reverse=False)
	
	result = ''
	for x in clean:
		result = result + str(x['PhoneNumber'])+','
	result = result[:-1]
	print (result)

if __name__ == '__main__':
	main()
