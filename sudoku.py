import numpy as np

grid = [[ 0, 0, 0, 0, 0, 0, 2, 0, 0],
		[ 0, 8, 0, 0, 0, 7, 0, 9, 0],
		[ 6, 0, 2, 0, 0, 0, 5, 0, 0],
		[ 0, 7, 0, 0, 6, 0, 0, 0, 0],
		[ 0, 0, 0, 9, 0, 1, 0, 0, 0],
		[ 0, 0, 0, 0, 2, 0, 0, 4, 0],
		[ 0, 0, 5, 0, 0, 0, 6, 0, 3],
		[ 0, 9, 0, 4, 0, 0, 0, 7, 0],
		[ 0, 0, 6, 0, 0, 0, 0, 0, 0]]

def possible(y,x,n):
	global grid
	#check row
	if n in grid[y]:
		return False
	#check column
	for r in range(9):
		if grid[r][x] == n:
			return False
	#check box
	row = (y//3)*3
	col = (x//3)*3
	for r in range(row, row+3):
		for c in range(col, col+3):
			if grid[r][c] == n:
				return False
	#otherwise
	return True

def next_slot():
	global grid
	for r in range(9):
		for c in range(9):
			if grid[r][c] == 0:
				return r,c
	return None, None

def Solver():
	global grid
	y,x = next_slot()
	if y == None:
		print(np.matrix(grid))
		return True
	for n in range(1,10):
		if possible(y,x,n):
			grid[y][x] = n
			if Solver():
				return True
			else:
				grid[y][x] = 0
	return False
	for n in range(1,10):
		count = 0
		#check row
		for c in range(9):
			if grid[y][c]==0 and possible(y,c,n):
				slot = c
				count += 1
		if count == 1 and slot == x:
			return (y,c,n)
		#check column
		for r in range(9):
			if grid[r][x]==0 and possible(r,x,n):
				slot = r
				count += 1
		if count == 1 and slot == y:
			return (r,x,n)

def Simplifier():
	global grid
	while True:
		t = grid.copy()
		for n in range(1,10):
			#check row
			for y in range(9):
				count = 0
				for x in range(9):
					if grid[y][x] == 0 and possible(y,x,n):
						col = x
						count += 1
				if count == 1:
					grid[y][col] = n
			#check column
			for x in range(9):
				count = 0
				for y in range(9):
					if grid[y][x] == 0 and possible(y,x,n):
						row = y
						count += 1
				if count == 1:
					grid[row][x] = n
			#check box
			for i in [0,3,6]:
				for j in [0,3,6]:
					count = 0
					row = i
					col = j
					for y in range(row,row+3):
						for x in range(col,col+3):
							if grid[y][x] == 0 and possible(y,x,n):
								slot = (y,x)
								count += 1
					if count == 1:
						r,c = slot
						grid[r][c] = n
		if t == grid:
			break
	return np.matrix(grid)

Simplifier()
Solver()