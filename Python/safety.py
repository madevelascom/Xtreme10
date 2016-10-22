__author__ = 'madevelasco'

import fileinput

def common_sequence(sequence, i, j, k):
	if sequence[i:j+1] == (sequence[k:(k+(j-i+1))]):
		print ('Y')
	else:
		print('N')

def replace_sequence(sequence,original, i, j, k):
	replace_seq = original[k:(k+(j-i+1))]
	sequence.replace(replace_seq, sequence[k:k+(j-i+1)], 1)	
	return sequence

def alter_letters(sequence, i, j):
	alter = ''
	for z in range(i, j):
		alter = alter+str(chr(ord(sequence[z])+1))
	sequence.replace(alter.lower(), sequence[i:j+1], 1)
	return sequence

def main():
	first = True
	second = True
	password = ''
	original = ''
	for line in fileinput.input():
		line = str(line)
		(line).strip()
		if (first):
			password = line
			original = line
			first = False
		elif(second):
			second = False
		else:
			orden = line.split()
			if (orden[0] == '1'):
				common_sequence(password, int(orden[1]), int(orden[2]), int(orden[3]))
			elif(orden[0] == '2'):
				replace_sequence(password, original, int(orden[1]), int(orden[2]), int(orden[3]))
			else:
				alter_letters(password, int(orden[1]), int(orden[2]))

if __name__ == '__main__':
	main()