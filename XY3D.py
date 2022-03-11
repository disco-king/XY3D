def undo(lst, num):
	lst[num[0]][num[1]][num[2]] = 0
	printm(lst)

def check_num(move):
	if not move[0].isdigit() or not move[1].isdigit() or not move[2].isdigit():
		return(True)
	n1, n2, n3 = int(move[0]), int(move[1]), int(move[2])
	if n1 > 3 or n1 < 1 or n2 > 3 or n2 < 1 or n3 > 3 or n3 < 1:
		return(True)

def printm(lst):
	print()
	for z in range(3):
		for y in range(3):
			print(' ' * y, end='')
			for x in range(3):
				print(lst[z][y][x],end='   ')
			print()
		print()


def get_num(f1, f2):
	if f1 < f2:
		z = 2
	elif f1 > f2:
		z = 0
	else:
		z = f1
	return(z)


def check_win(lst, map2, map1):
	z = get_num(map1[0], map2[0])
	y = get_num(map1[1], map2[1])
	x = get_num(map1[2], map2[2])
	if lst[z][y][x] == lst[map1[0]][map1[1]][map1[2]]:
		return(lst[z][y][x])
	return("N")


def check_two(lst, map0, minus, var):
	res = "N"
	map1 = map0.copy()
	map1[minus] -= 1
	z, y, x = map0[0], map0[1], map0[2]
	for i in range(3):
		map1[var] = i
		if lst[z][y][x] == lst[map1[0]][map1[1]][map1[2]] and lst[map1[0]][map1[1]][map1[2]] != 0:
			res = check_win(lst, [z, y, x], [map1[0], map1[1], map1[2]])
	return(res) 


def get_it(a, b):
	if a + b == 1:
		c = 2
	elif a + b == 2:
		c = 1
	else:
		c = 0
	return(c)


def check_thre(lst, map0, minus, var):
	map1 = map0.copy()
	map1[minus] -= 1
	v = get_it(minus, var)
	z, y, x = map0[0], map0[1], map0[2]
	for i in range(3):
		for j in range(3):
			map1[var] = j
			map1[v] = i
			if lst[z][y][x] == lst[map1[0]][map1[1]][map1[2]] and lst[map1[0]][map1[1]][map1[2]] != 0:
				res = check_win(lst, [z, y, x], [map1[0], map1[1], map1[2]])
				if res != "N":
					return(res)
	return("N")


def check_field(lst):
	res = "N"
	for z in range(3):
		for y in range(3):
			for x in range(3):
				if (y == 0 or y == 2) and x == 1 and lst[z][y][x] != 0:
					if z == 1:
						res = check_two(lst, [z, y, x], 0, 2)
						if res != "N":
							return(res)
						res = check_two(lst, [z, y, x], 2, 0)
						if res != "N":
							return(res)
					elif lst[z][y][x] == lst[z][y][x-1]:
						res = check_win(lst, [z, y, x], [z, y, x-1])
						if res != "N":
							return(res)
				if (x == 0 or x == 2) and y == 1 and lst[z][y][x] != 0:
					if z == 1:
						res = check_two(lst, [z, y, x], 0, 1)
						if res != "N":
							return(res)
						res = check_two(lst, [z, y, x], 1, 0)
						if res != "N":
							return(res)
					elif lst[z][y][x] == lst[z][y-1][x]:
						res = check_win(lst, [z, y, x], [z, y-1, x])
						if res != "N":
							return(res)
				point = x*x + y*y
				if z == 1 and point in [0, 4, 8] and lst[z][y][x] != 0:
					if lst[z][y][x] == lst[z-1][y][x]:
						res = check_win(lst, [z, y, x], [z-1, y, x])
						if res != "N":
								return(res)
				if x == 1 and y == 1 and lst[z][y][x] != 0:
					if z == 1:
						res = check_thre(lst, [z, y, x], 0, 1)
						if res != "N":
							return(res)
						res = check_thre(lst, [z, y, x], 1, 0)
						if res != "N":
							return(res)
						res = check_thre(lst, [z, y, x], 2, 1)
						if res != "N":
							return(res)
					else:
						res = check_two(lst, [z, y, x], 1, 2)
						if res != "N":
							return(res)
						res = check_two(lst, [z, y, x], 2, 1)
						if res != "N":
							return(res)
	return(res)


lst = [[[0 for p in range(3)] for i in range(3)] for j in range(3)]
print('GREETINGS', '\n', '\n', 'This is the game of XY3D', sep='')
printm(lst)

xy = "XY"
move_count = 0
undo_dic = {}

while True:
	figure = move_count % 2
	print('Your move,', xy[figure])
	move = input().split()

	if len(move) == 0:
		continue

	elif move[0] == 'over':
		print('GAME OVER')
		break

	elif move[0] == 'undo':
		undo(lst, undo_dic[move_count - 1])
		move_count -= 1
		continue

	elif len(move) != 3 or check_num(move):
		print('Wrong move. Try again!')
		continue

	num_z, num_y, num_x = (int(move[0]))-1, (int(move[2]))-1, (int(move[1]))-1
	if lst[num_z][num_y][num_x] != 0:
		print('Wrong move. Try again!')
		continue
	undo_dic[move_count] = [num_z, num_y, num_x]
	lst[num_z][num_y][num_x] = xy[figure]

	printm(lst)
	res = check_field(lst)
	if res != "N":
		print(res, ' wins!')
		print('Play again? [y/n]')
		ans = input()
		while ans != "y" and ans != "n":
			print('Sorry, wrong input', '\n', 'Play again? [y/n]', sep='')
			ans = input()
		if ans == "y":
			for z in range(3):
				for y in range(3):
					for x in range(3):
						lst[z][y][x] = 0
			move_count = 0
			printm(lst)
			continue
		if ans == "n":
			print('GAME OVER')
			break
	move_count += 1
