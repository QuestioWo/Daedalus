cells = []

stack = []

wall = "|"
ceiling = "--"
corner = "*"
gap = "  "

m = 31
a = 17
c = 13
seed = 1234

cell_length = 7

def build(width, height) :
	for i in range(height) :
		for j in range(width) :
			cells.append(i) #y = i
			cells.append(j) #x = j

			cells.append(0) #visited = 2

			cells.append(0) #N = 3
			cells.append(0) #E = 4
			cells.append(0) #S = 5
			cells.append(0) #W = 6

def print_cells() :
	for i in range(height) :
		for j in range(width) :
			if cells[(i * cell_length * width) + j * cell_length + 3] == 0 :
				if cells[(i * cell_length * width) + j * cell_length + 1] == 0 :
					print(corner, end="")
				
				print(ceiling + corner, end="")
			else :
				if cells[(i * cell_length * width) + j * cell_length + 1] == 0 :
					print(corner, end="")

				print(gap + corner, end="")

		print("")

		for j in range(width) :
			if cells[(i * cell_length * width) + j * cell_length + 6] == 0 :
				print(wall + gap, end="")
			else :
				print(" " + gap, end="")

			if cells[(i * cell_length * width) + j * cell_length + 1] == width - 1 :
				if cells[(i * cell_length * width) + j * cell_length + 4] == 0 :
					print(wall, end="")
				else :
					print(" ", end="")

		for j in range(width) :
			if cells[(i * cell_length * width) + j * cell_length] == height - 1 :
				if j == 0 :
					print("")
				if cells[(i * cell_length * width) + j * cell_length + 5] == 0 :
					if cells[(i * cell_length * width) + j * cell_length + 1] == 0 :
						print(corner, end="")
					
					print(ceiling + corner, end="")
				else :
					if cells[(i * cell_length * width) + j * cell_length + 1] == 0 :
						print(corner, end="")

					print(gap + corner, end="")
			else :
				break

		print("")

def random_num() :
	global seed
	seed = (seed * a + c) % m

def generateMaze(cell_y, cell_x, first=False):
	# base case
	if len(stack) == 0 and not first :
		return None

	# recusive step
	else :
		cells[(cell_y * cell_length * width) + cell_x * cell_length + 2] = 1
		chosen_cell = None

		while True :
			# random generator
			random_num()
			random_int = seed % 4

			chosen_cell_y, chosen_cell_x = choose_cell(cell_y, cell_x, random_int)
			if chosen_cell_y < height and chosen_cell_y > -1 :
				stack.append(cell_y)
				stack.append(cell_x)
				return generateMaze(chosen_cell_y, chosen_cell_x)

			else :
				if chosen_cell_y == -1 :
					prev_cell_x = stack.pop()
					prev_cell_y = stack.pop()
					return generateMaze(prev_cell_y, prev_cell_x)


def choose_cell(cell_y, cell_x, random_int) :
	bad = True
	if cell_y > 0 and not cells[(((cell_y - 1) * cell_length) * width) + cell_x * cell_length + 2] :
		bad = False
		if random_int == 0 :
			cells[(cell_y * cell_length * width) + cell_x * cell_length + 3] = 1
			cells[(((cell_y - 1) * cell_length) * width) + cell_x * cell_length + 5] = 1
			return (cell_y - 1, cell_x)

	if cell_x < width - 1 and not cells[(cell_y * cell_length * width) + ((cell_x + 1) * cell_length) + 2] :
		bad = False
		if random_int == 1 :
			cells[(cell_y * cell_length * width) + cell_x * cell_length + 4] = 1
			cells[(cell_y * cell_length * width) + ((cell_x + 1) * cell_length) + 6] = 1
			return (cell_y, cell_x + 1)

	if cell_y < height - 1 and not cells[(((cell_y + 1) * cell_length) * width) + cell_x * cell_length + 2] :
		bad = False
		if random_int == 2 :
			cells[(cell_y * cell_length * width) + cell_x * cell_length + 5] = 1
			cells[(((cell_y + 1) * cell_length) * width) + cell_x * cell_length + 3] = 1
			return (cell_y + 1, cell_x)

	if cell_x > 0 and not cells[(cell_y * cell_length * width) + ((cell_x - 1) * cell_length) + 2] :
		bad = False
		if random_int == 3 :
			cells[(cell_y * cell_length * width) + cell_x * cell_length + 6] = 1
			cells[(cell_y * cell_length * width) + ((cell_x - 1) * cell_length) + 4] = 1
			return (cell_y, cell_x - 1)

	if bad == False :
		return (height + 1, width + 1)
	else :
		return (-1, -1)


if __name__ == "__main__" :
	width = 4
	height = 4

	build(width, height)

	generateMaze(0, 0, True)

	print_cells()
