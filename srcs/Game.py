import sys


class Game(object):
	def __init__(self, height, width, win_length, t_time, g_time, game_status):
		self.height = int(height)
		self.width = int(width)
		self.win_length = int(win_length)
		self.t_time = int(t_time) # Total time
		self.g_time = int(g_time) # Gain time per round
		self.game_status = int(game_status) # 0 = in progress / 1 = finish
		self.tab = self.create_tab()
		self.max_height = 0
		self.binary = self.create_tab()

	def status(self): # DONE
		return (self.game_status)

	def create_tab(self): # DONE
		tab = []
		
		for _ in range(0, self.height):
			line = [0] * self.width
			tab.append(line)

		return (tab)

	def show_tab(self): # DONE (debug)
		for i in range(0, self.height):
			print(self.tab[i], file=sys.stderr)

	def show_tab_binary(self): # DONE (debug)
		for i in range(0, self.height):
			print('', file=sys.stderr)
			for j in range(0, self.width):
				if self.binary[i][j] == 9:
					print("\033[;31m" + str(self.binary[i][j]) + "\033[;0m", file=sys.stderr, end=' ')
				else:
					print(self.binary[i][j], file=sys.stderr, end=' ')
		print('\n', file=sys.stderr)

	def put_in_tab(self, width, player): # DONE
		n = 0
		while self.tab[n][width] == 0 and n < self.height - 1:
			n += 1
			# print(str(n) + "\n")
		if self.tab[n][width] != 0:
			n -= 1
		self.tab[n][width] = 9
		self.binary[n][width] = 9
		if n > self.max_height:
			self.max_height = n
	# 8 c les mechants
	# 9 c nous

	# TODO :
	# . Clean le code lol
	def is_winning(self, y, x):
		t_y = y
		t_x = x
		count = 0
		if y + 1 < self.height and y - 1 > 0  and (self.tab[y + 1][x] == 8 or self.tab[y - 1][x] == 8): #top to down
			while y + 1 < self.height and self.binary[t_y][X] == 8: #top
				t_y += 1
				count += 1
			t_y = y
			t_x = x
			while y - 1 > 0 and self.binary[t_y][x] == 8: #down
				t_y -= 1
				count += 1
			if count == self.win_lenght:
				print(x) #win
				return 1
		#count = 0
		#t_y = y
		#t_x = x
		#tt_y = y
		#tt_x = x

		#if y - 1 > 0 and self.tab[y - 1][x] == 8: #down to top
		#	while y - 1 > 0 and self.binary[t_y][x] == 8: #down
		#		t_y -= 1
		#		count += 1
		#	while y + 1 < self.height and self.binary[tt_y][x] == 8: #top
		#		tt_y += 1
		#		count += 1
		#	if count == self.win_lenght:
		#		print(x) #win
		#		return 1
		count = 0
		t_y = y
		t_x = x

		if x + 1 < self.width and x - 1 > 0 and (self.binary[y][x + 1] == 8 or self.binary[y][x - 1] == 8): #right to left
			while x + 1 < self.width and self.binary[y][t_x] == 8: #right
				t_x += 1
				count += 1
			t_y = y
			t_x = x
			while x - 1 > 0 and self.binary[y][t_x] == 8: #left
				t_x -= 1 
				count += 1
			if count == self.win_lenght:
				print(x) #win
				return 1
		#count = 0
		#t_y = y
		#t_x = x
		#tt_y = y
		#tt_x = x
#
		#if x - 1 < self.width and self.binary[y][x - 1] == 8: #left to right
		#	while x - 1 > 0 and self.binary[y][t_x] == 8: #left
		#		t_x -= 1
		#		count += 1
		#	while x + 1  < self.width and self.binary[y][tt_x] == 8: #right
		#		tt_x += 1 
		#		count += 1
		#	if count == self.win_lenght:
		#		print(x) #win
		#		return 1
		count = 0
		t_y = y
		t_x = x
		tt_y = y
		tt_x = x
		if x - 1 > 0 and y + 1 < self.height and self.binary[y + 1][x - 1] == 8: #left top to down right
			while x - 1 > 0 and y + 1 < self.height and self.binary[t_x][t_y] == 8:
				t_x -= 1
				t_y += 1
				count += 1
			while x + 1 < self.width and y - 0 > 0 and self.binary[tt_x][tt_y] == 8:
				tt_x += 1
				tt_y -= 1
				count += 1
			if count == self.win_lenght:
				print(x) #win
				return 1
			
		return 0

	def binary_mask(self):
		x_one = 0
		y_one = 0

		self.show_tab_binary()

		# Parcours le binary mask
		for y in range(0, self.height):
			for x in range(0, self.width):
				if self.binary[y][x] == 9:
					
					# Find right and project line to right
					for i in range(0, self.win_length):
						# Check for a O
						if x + i < self.width and self.binary[y][x + i] == 8:
							break
					
						# Fill with score start at x + win_length
						if x + i < self.width and self.binary[y][x + i] >= 0 and self.binary[y][x + i] <= 3:
							print(self.binary[y][x + i])
							# Project at x + win_length - 1
							occurence = 0
							for j in range(x + self.win_length - 1, x, -1):
								if self.binary[y][j] >= 0 and self.binary[y][j] <= 3:
									occurence += 1
							
							if occurence >= 1:
							# Project at x + win_length - occurence
								for j in range(x + self.win_length - occurence + 1, x, -1):
									if self.binary[y][j] != 9:
										self.binary[y][j] = j - x
					
								
								
							


					# Find diagonale right and project line to diagonale right
					for i in range(0, self.win_length):
						return 1
					
		return 1
		


	# # Return an array with each occurence of potential defense, if tab is empty -> switch to attack occurence
	# def find_occurences_defense(self):
	# 	defenses = []

	# 	occurence = []
	# 	for y in range(self.max_height, self.height):
	# 		for x in range(0, self.width):
	# 			if self.tab[y][x] == '2':
	# 				if find_end_occurence(x, y) == -1:
	# 					continue 
					
	# 				return 0
	

	# 	return 0

	# # Try to find an occurence with winning length
	# def find_end_occurence(self, x, y):
	# 	occurence = []

	# 	start = 0
	# 	end = 0
	# 	orentation ='
	# 	# Check length of potential occurence
	# 	if self.height - y < self.win_length:
	# 		return -1

	# 	# Right search
	# 	for i in range(0, self.win_length):
	# 		if 

	# 	return 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 