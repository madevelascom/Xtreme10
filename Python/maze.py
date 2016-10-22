__author__ = 'madevelasco'

import fileinput

def create_board(sq_size):
	board = [['x' for x in range(sq_size+2)] for y in range(sq_size+2)] 
	return board

def board_discover(board, row, col):
	board[row][col] = 'o'
	return board

def play_game(board, row, col, visited):
	surs = 	((row-1, col), (row, col-1), (row, col+1),(row+1, col))
	for(surr_row, surr_col) in surs:
		if ((surr_row, surr_col) not in visited and board[surr_row][surr_col]=='o'):
			visited.append((surr_row, surr_col))
			x = surr_row+1
			y = len(board)-2
			if(x == y):
				return True
			else:
				return play_game(board, surr_row, surr_col, visited)

def main():
	sq_size = 0
	first = True
	game = [[]]
	i, j= 0, 1
	result = []
	for line in fileinput.input():
		line = str(line)
		(line).strip()
		if (first):
			sq_size = int(line)
			game = create_board(sq_size)
			first = False
		else:
			i += 1
			coords = line.split()
			if(coords[0] == '-1'):
				result.append(-1)
			else:
				game = board_discover(game, int(coords[0]), int(coords[1]))
				for z in range(1, sq_size+1):
					visited = []
					if(play_game(game, 1, z, visited)):
						result.append(i)
						break
						break
	print(result[0])

if __name__ == '__main__':
	main()