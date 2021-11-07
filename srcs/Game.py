import sys
import math

# 8 -> Les autres
# 9 -> Nous

# TODO : supprimer la fonction place_point et tout faire dans la meme boucle, des qu'on pose un 1, on check direct si c'est un winning move -> si oui on le pose
# TODO : dans place_point, implementer pour savoir les is_winning de l'adversaire et les contrer inevitablement
# TODO : optimisation possible quand on trouve un 1, on cherche la len de 9 si on pose un (pour eviter de poser un point a chaque fois qu'on trouve le premier 1)
# TODO : grosse optimisation sur binary_a et binary_d qu'on traine partout -> eviter de trainer des copies dans chaque fonction et faire ca nativament


class Game(object):
	def __init__(self, height, width, win_length, t_time, g_time, game_status):
		self.height = int(height)
		self.width = int(width)
		self.win_length = int(win_length)
		self.t_time = int(t_time)  # Total time
		self.g_time = int(g_time)  # Gain time per round
		self.game_status = int(game_status)  # 0 = in progress / 1 = finish
		self.tab = []
		self.max_height = 0
		self.binary_a = []
		self.binary_d = []
		self.start = True

	def status(self):  # DONE
		return (self.game_status)

	def create_tab(self):  # DONE
		for _ in range(0, self.height):
			line = []
			for i in range(0, self.width):
				line.append(0)
			self.tab.append(line)

	def create_tab_binary(self):  # DONE
		for _ in range(0, self.height):
			line = []
			line1 = []
			for i in range(0, self.width):
				line.append(0)
				line1.append(0)
			self.binary_a.append(line)
			self.binary_d.append(line1)

	def show_tab(self):  # DONE (debug)
		for i in range(0, self.height):
			print(self.tab[i], file=sys.stderr)

	def show_tab_binary(self):  # DONE (debug)
		print("\033[;31m DEFENSIVE !\033[;0m", file=sys.stderr)
		for i in range(0, self.height):
			print('', file=sys.stderr)
			for j in range(0, self.width):
				if self.binary_d[i][j] == 9:
					print("\033[;34m" + str(self.binary_d[i][j]) +
						  "\033[;0m", file=sys.stderr, end=' ')
				elif self.binary_d[i][j] == 1:
					print("\033[;32m" + str(self.binary_d[i][j]) +
						  "\033[;0m", file=sys.stderr, end=' ')
				elif self.binary_d[i][j] == 2:
					print("\033[;33m" + str(self.binary_d[i][j]) +
						  "\033[;0m", file=sys.stderr, end=' ')
				elif self.binary_d[i][j] == 8:
					print("\033[;35m" + str(self.binary_d[i][j]) +
						  "\033[;0m", file=sys.stderr, end=' ')
				elif self.binary_d[i][j] >= 3 and self.binary_d[i][j] <= 7:
					print("\033[;31m" + str(self.binary_d[i][j]) +
						  "\033[;0m", file=sys.stderr, end=' ')
				else:
					print(self.binary_d[i][j], file=sys.stderr, end=' ')
		print('\n', file=sys.stderr)

		print("\033[;31m ATTACK !\033[;0m", file=sys.stderr)
		for i in range(0, self.height):
			print('', file=sys.stderr)
			for j in range(0, self.width):
				if self.binary_a[i][j] == 9:
					print("\033[;34m" + str(self.binary_a[i][j]) +
						  "\033[;0m", file=sys.stderr, end=' ')
				elif self.binary_a[i][j] == 1:
					print("\033[;32m" + str(self.binary_a[i][j]) +
						  "\033[;0m", file=sys.stderr, end=' ')
				elif self.binary_a[i][j] == 2:
					print("\033[;33m" + str(self.binary_a[i][j]) +
						  "\033[;0m", file=sys.stderr, end=' ')
				elif self.binary_a[i][j] == 8:
					print("\033[;35m" + str(self.binary_a[i][j]) +
						  "\033[;0m", file=sys.stderr, end=' ')
				elif self.binary_a[i][j] >= 3 and self.binary_a[i][j] <= 7:
					print("\033[;31m" + str(self.binary_a[i][j]) +
						  "\033[;0m", file=sys.stderr, end=' ')
				else:
					print(self.binary_a[i][j], file=sys.stderr, end=' ')
		print('\n', file=sys.stderr)

	def put_in_tab(self, width, player):  # DONE
		n = 0
		while self.tab[n][width] == 0 and n < self.height - 1:
			n += 1
			# print(str(n) + "\n")
		if self.tab[n][width] != 0:
			n -= 1
		self.tab[n][width] = player
		self.binary_a[n][width] = player
		self.binary_d[n][width] = player
		if n > self.max_height:
			self.max_height = n

	def is_winning(self, y, x):
		t_y = y
		t_x = x
		count = 0
		# top to down
		if y + 1 < self.height and (self.binary_a[y + 1][x] == 9):
			while t_y + 1 < self.height and self.binary_a[t_y + 1][x] == 9:  # top
				t_y += 1
				count += 1
		t_y = y
		t_x = x
#if y - 1 > 0 and (self.binary_a[y - 1][x] == 9): #Useless
		#	print("down") 
		#	while t_y - 1 > 0 and self.binary_a[t_y - 1][x] == 9:  # down
		#		t_y -= 1
#count += 1
		# top to down verif
		if count == self.win_length:
			print(x)  # win
			return 1
		count = 0
		t_y = y
		t_x = x
		
		# right to left
		if x + 1 < self.width and self.binary_a[y][x + 1] == 9:
			while t_x + 1 < self.width and self.binary_a[y][t_x + 1] == 9:  # right
				t_x += 1
				count += 1
		t_y = y
		t_x = x
		# left to right
		if x - 1 > 0 and self.binary_a[y][x - 1] == 9:
			while t_x - 1 > 0 and self.binary_a[y][t_x - 1] == 9:  # left
				t_x -= 1
				count += 1
		# right and left verif
		if count == self.win_length:
			print(x)  # win
			return 1
		count = 0
		t_y = y
		t_x = x

		# left top to down right
		if x - 1 > 0 and y + 1 < self.height and self.binary_a[y + 1][x - 1] == 9:
			while t_x - 1 > 0 and t_y + 1 < self.height and self.binary_a[t_y + 1 ][t_x - 1] == 9:
				t_x -= 1
				t_y += 1
				count += 1
			t_y = y
			t_x = x
		# right down to top left
		if x + 1 < self.width and y - 1 > 0 and self.binary_a[y - 1][x + 1] == 9:
			while t_x + 1 < self.width and t_y - 1 > 0 and self.binary_a[t_y - 1][t_x + 1] == 9:
				t_x += 1
				t_y -= 1
				count += 1
		if count == self.win_length:
			print(x)  # win
			return 1

		#right down to left down 
		if x - 1 < self.width and y - 1 < self.height and self.binary_a[y - 1][x - 1] == 9:
			while t_x - 1 > 0 and t_y - 1 > 0 and self.binary_a[t_y - 1][t_x - 1] == 9:
				t_x -= 1
				t_y -= 1
				count += 1
			t_y = y
			t_x = x
		#top left to right top
		if x + 1 < self.width and y + 1 < self.height and self.binary_a[y + 1][x + 1] == 9:
			while t_x + 1 < self.width and t_y + 1 < self.height and self.binary_a[t_y + 1][t_x + 1] == 9:
				t_x += 1
				t_y += 1
				count += 1
		if count == self.win_length:
			print(x)  # win
			return 1
		return 0


	def is_defeat(self, y, x):
		t_y = y
		t_x = x
		count = 0
		# top to down
		if y + 1 < self.height and (self.binary_d[y + 1][x] == 8):
			while t_y + 1 < self.height and self.binary_d[t_y + 1][x] == 8:  # top
				t_y += 1
				count += 1
		t_y = y
		t_x = x
#if y - 1 > 0 and (self.binary_d[y - 1][x] == 8): #Useless
		#	print("down") 
		#	while t_y - 1 > 0 and self.binary_d[t_y - 1][x] == 8:  # down
		#		t_y -= 1
#count += 1
		# top to down verif
		if count == self.win_length:
			print(x)  # win
			return 1
		count = 0
		t_y = y
		t_x = x
		
		# right to left
		if x + 1 < self.width and self.binary_d[y][x + 1] == 8:
			while t_x + 1 < self.width and self.binary_d[y][t_x + 1] == 8:  # right
				t_x += 1
				count += 1
		t_y = y
		t_x = x
		# left to right
		if x - 1 > 0 and self.binary_d[y][x - 1] == 8:
			while t_x - 1 > 0 and self.binary_d[y][t_x - 1] == 8:  # left
				t_x -= 1
				count += 1
		# right and left verif
		if count == self.win_length:
			print(x)  # win
			return 1
		count = 0
		t_y = y
		t_x = x

		# left top to down right
		if x - 1 > 0 and y + 1 < self.height and self.binary_d[y + 1][x - 1] == 8:
			while t_x - 1 > 0 and t_y + 1 < self.height and self.binary_d[t_y + 1 ][t_x - 1] == 8:
				t_x -= 1
				t_y += 1
				count += 1
			t_y = y
			t_x = x
		# right down to top left
		if x + 1 < self.width and y - 1 > 0 and self.binary_d[y - 1][x + 1] == 8:
			while t_x + 1 < self.width and t_y - 1 > 0 and self.binary_d[t_y - 1][t_x + 1] == 8:
				t_x += 1
				t_y -= 1
				count += 1
		if count == self.win_length:
			print(x)  # win
			return 1

		#right down to left down 
		if x - 1 < self.width and y - 1 < self.height and self.binary_d[y - 1][x - 1] == 8:
			while t_x - 1 > 0 and t_y - 1 > 0 and self.binary_d[t_y - 1][t_x - 1] == 8:
				t_x -= 1
				t_y -= 1
				count += 1
			t_y = y
			t_x = x
		#top left to right top
		if x + 1 < self.width and y + 1 < self.height and self.binary_d[y + 1][x + 1] == 8:
			while t_x + 1 < self.width and t_y + 1 < self.height and self.binary_d[t_y + 1][t_x + 1] == 8:
				t_x += 1
				t_y += 1
				count += 1
		if count == self.win_length:
			print(x)  # win
			return 1
		return 0


	def binary_mask(self, tab, target, target2):
		# Parcours le binary mask
		for y in range(self.max_height - 1, self.height):
			for x in range(0, self.width):
				if tab[y][x] == target:

					# Find top and project line to the top
					for i in range(0, self.win_length):
						# Check for a O
						if y - i >= 0 and tab[y - i][x] == target2:
							break

						# Fill with score at y + win_length
						if y - i >= 0 and tab[y - i][x] >= 0 and tab[y - i][x] <= 7:

							# Project at y + win_length - 1
							occurence = 0
							for j in range(y - self.win_length + 1, y, 1):
								if j >= 0 and tab[j][x] >= 0 and tab[j][x] <= 7:
									occurence += 1
							if occurence >= 1 and tab[y - 1][x] != 9 and tab[y - 1][x] != 8:
								# Project at x + win_length - occurence
								for j in range(y - occurence, y, 1):
									# Check for winning place
									if y - j == 1:
										if self.is_winning(j, x):
											exit(1)
										else:
											tab[j][x] = y - j
								break

					# Find right and project line to right
					for i in range(0, self.win_length):
						# Check for a O
						if x + i < self.width and tab[y][x + i] == target2:
							break

						# Fill with score start at x + win_length
						if x + i < self.width and tab[y][x + i] >= 0 and tab[y][x + i] <= 7:

							# Project at x + win_length - 1
							occurence = 0
							for j in range(x + self.win_length - 1, x, -1):
								if j < self.width and tab[y][j] >= 0 and tab[y][j] <= 7:
									occurence += 1

							if occurence >= 1:
								# Project at x + win_length - occurence
								for j in range(x + occurence, x, -1):
									if tab[y][j] != 9 and tab[y][j] != 8:
										cost = self.find_cost_below(j - x,  y, tab, x)
										print('le cost = ' + str(cost) + ' et le x = ' + str(x))
										if cost == 1:
											if self.is_winning(y, j):
												exit(1)
											else:
												tab[y][j] = cost
										# if cost <= 2 and y == self.height - 1:
										# 	tab[y][j] = j - x
										# else:
										# 	tab[y][j] = cost

					# Find left and project line to left
					for i in range(x, 0, -1):
						# Check for a O
						if x - i >= 0 and tab[y][x - i] == target2:
							break

						# Fill with score start at x - win_length
						if x - i >= 0 and tab[y][x - i] >= 0 and tab[y][x - i] <= 7:

							# Project at x + win_length - 1
							occurence = 0
							for j in range(x - self.win_length + 1, x, 1):
								if j >= 0 and tab[y][j] >= 0 and tab[y][j] <= 7:
									occurence += 1

							if occurence >= 1:
								# Project at x + win_length - occurence
								for j in range(x - occurence, x, 1):
									if tab[y][j] != 9 and tab[y][j] != 8:
										cost = self.find_cost_below(x - j,  y, tab, x)
									
										if cost == 1:
											if self.is_winning(y, j):
												exit(1)
											else:
												tab[y][j] = cost
								break

					# # Find diagonale right and project line to diagonale right
					# if y >= self.win_length - 1 and self.width - x >= self.win_length - 1:
					# 	for i in range(0, self.win_length):
					# 		# Check for a O
					# 		if x + i < self.width and y - i >= 0 and tab[y - i][x + i] == target2:
					# 			break

					# 		# Search for valid value
					# 		if x + i < self.width and y - i >= 0 and tab[y - i][x + i] >= 0 and tab[y - i][x + i] <= 7:

					# 			# Project at x + win_length
					# 			occurence = 0
					# 			for j in range(0, self.win_length - 1):
					# 				if x + i < self.width and y - i >= 0 and tab[y - i][x + i] >= 0 and tab[y - i][x + i] <= 7:
					# 					occurence += 1
					# 			if occurence >= 1:
					# 				# Project at x + occurence and y - occurence
					# 				for j in range(occurence - 1, 0, -1):
					# 					if tab[y - j][x + j] != 9 and tab[y - j][x + j] != 8:
					# 						cost = self.find_cost_below_right(x + j, y - j, tab)
					# 						# print('l')
					# 						if cost == 1:
					# 							if self.is_winning(y - j, x + j):
					# 								exit(1)
					# 							else:
					# 								tab[y - j][x + j] = cost

					# # Find diagonale left and project line to diagonale left
					# if y >= self.win_length - 1 and x >= self.win_length - 1:
					# 	for i in range(0, self.win_length):
					# 		# Check for a O
					# 		if x - i >= 0 and y - i >= 0 and tab[y - i][x - i] == 8:
					# 			break

					# 		# Search for valid value
					# 		if x - i >= 0 and y - i >= 0 and tab[y - i][x - i] >= 0 and tab[y - i][x - i] <= 7:

					# 			# Project at x - win_length
					# 			occurence = 0
					# 			for j in range(0, self.win_length - 1):
					# 				if x - i >= 0 and y - i >= 0 and tab[y - i][x - i] >= 0 and tab[y - i][x - i] <= 7:
					# 					occurence += 1

					# 			if occurence >= 1:
					# 				# Project at x - occurence and y - occurence
					# 				for j in range(occurence - 1, 0, -1):
					# 					if tab[y - j][x - j] != 9 and tab[y - j][x - j] != 8:
					# 						cost = self.find_cost_below_right(x + j, y - j, tab)
					# 						if cost == 1:
					# 							if self.is_winning(y - j, x - j):
					# 								exit(1)
					# 							else:
					# 								tab[y - j][x - j] = cost

		return 1

	# Define the cost for diagonale line

	def find_cost_below_right(self, x, y, tab):
		cost = 0
		
		# Optimisation, instant return cost if y - 1 == target
		if x <= self.width - 1 and y - 1 >= 0 and y - 1 <= self.height - 1 and (tab[y - 1][x] == 9 or tab[y - 1][x] == 8):
			return 1

		# Search below the given coordinates
		for i in range(0, self.height - y):
			if x <= self.width - 1 and y - 1 >= 0 and y - 1 <= self.height - 1 and tab[self.height - i - 1][x] != 9 and tab[self.height - i - 1][x] != 8:
				cost += 1

		# Add precedent cost from previous coordinates
		if y + 1 <= self.height - 1 and x - 1 >= 0 and (tab[y + 1][x - 1] != 9 or tab[y + 1][x - 1] != 8):
			cost = cost + tab[y + 1][x - 1]

		if cost >= 8:
			return 7
		return cost

	def find_cost_below_left(self, x, y, tab):
		cost = 0

		# Optimisation, instant return cost if y - 1 == 9
		if tab[y + 1][x] == 9 or tab[y + 1][x] == 8:
			return 1 

		# Search below the given coordinates
		for i in range(0, self.height - y):
			if tab[self.height + i - 1][x] != 9 and tab[self.height + i - 1][x] != 8:
				cost += 1

		# Add precedent cost from previous coordinates
		if y - 1 >= 0 and x + 1 <= self.width - 1 and tab[y - 1][x + 1] != 9:
			cost = cost + tab[y - 1][x + 1]

		if cost >= 8:
			return 7

		return cost

	def find_cost_below(self, x, y, tab, initial):
		cost = 0

		# Optimisation, instant return cost if y + 1 == 9 or 8
		if y + 1 < self.height and (tab[y + 1][x] == 9 or tab[y + 1][x] == 8):
			if initial >= 8:
				return 7
			else:
				return initial
		
		# Search below the given coordinates
		for i in range(0, self.height - y):
			if tab[self.height - i - 1][x] != 9 and tab[self.height - i - 1][x] != 8:
				cost += 1
			else:
				return cost

		if (initial + x) - initial >= 2:
			return 0
		return cost

	# Search for a winning point or a 1 defense
	def place_point(self):

		# If the game start place a point in the middle
		if self.start == True:
			self.binary_a[self.height - 1][int(self.width / 2)] = 9
			print(int(self.width / 2))
			self.put_in_tab(int(self.width / 2), 9)
			self.start = False

		# Find a winning point
		for y in range(0, self.height):
			for x in range(0, self.width):
				if self.binary_a[y][x] == 1:
					if self.is_winning(y, x) == 1:
						exit(1)

		# Find winning enemy point
		for y in range(0, self.height):
			for x in range(0, self.width):
				if self.binary_d[y][x] == 1:
					if self.is_defeat(y, x) == 1:
						return

		# Choose correct 1 possibility
		for y in range(0, self.height):
			for x in range(0, self.width):
				if self.binary_a[y][x] == 1:
					print(x)
					self.put_in_tab(int(x), 9)
					return


				
		












































				#count = 0
				#t_y = y
				#t_x = x
				#tt_y = y
				#tt_x = x
				#
				# if x - 1 < self.width and self.binary[y][x - 1] == 8: #left to right
				#	while x - 1 > 0 and self.binary[y][t_x] == 8: #left
				#		t_x -= 1
				#		count += 1
				#	while x + 1  < self.width and self.binary[y][tt_x] == 8: #right
				#		tt_x += 1
				#		count += 1
				#	if count == self.win_lenght:
				#		print(x) #win
				#		return 1
				#count = 0
				#t_y = y
				#t_x = x
				#tt_y = y
				#tt_x = x

				# if y - 1 > 0 and self.tab[y - 1][x] == 8: #down to top
				#	while y - 1 > 0 and self.binary[t_y][x] == 8: #down
				#		t_y -= 1
				#		count += 1
				#	while y + 1 < self.height and self.binary[tt_y][x] == 8: #top
				#		tt_y += 1
				#		count += 1
				#	if count == self.win_lenght:
				#		print(x) #win
				#		return 1
