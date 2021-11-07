import sys
import math
import random

# TOP DEFENCE - OK
# TOP WIN - OK


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
		self.tab = self.create_tab_binary()
		self.max_height = 0
		self.binary_a = self.create_tab_binary()
		self.binary_d = self.create_tab_binary()
		self.start = True

	def status(self):  # DONE
		return (self.game_status)

	def create_tab(self):  # DONE

		for _ in range(0, self.height):
			line = []
			for i in range(0, self.width):
				line.append(0)
			self.tab.append(line)

	def show_tab(self):
		for x in range(0, self.height):
			print(self.tab[x])

	def create_tab_binary(self):  # DONE
		matrix = []
		for r in range(0, self.height):
			matrix.append([0 for c in range(0, self.width)])

		return matrix

		# for _ in range(0, self.height):
		# 	line = []
		# 	line1 = []
		# 	for i in range(0, self.width):
		# 		line.append(0)
		# 		line1.append(0)
		# 	matrix.append(line)
		# 	self.binary_d.append(line1)

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
		# self.show_tab_binary()
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
		# self.show_tab_binary()

	def is_winning(self, y, x):
		t_y = y
		t_x = x
		count = 0
		# top to down
		if y + 1 < self.height and (self.binary_a[y + 1][x] == 9):
			# top
			while t_y + 1 < self.height and self.binary_a[t_y + 1][x] == 9:
				t_y += 1
				count += 1
		t_y = y
		t_x = x
		# top to down verif
		if count == self.win_length:
			print(x)  # win
			return 1
		count = 0
		t_y = y
		t_x = x

		# right to left
		if x + 1 < self.width and self.binary_a[y][x + 1] == 9:
			# right
			while t_x + 1 < self.width and self.binary_a[y][t_x + 1] == 9:
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
			while t_x - 1 > 0 and t_y + 1 < self.height and self.binary_a[t_y + 1][t_x - 1] == 9:
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

		# right down to left down
		if x - 1 < self.width and y - 1 < self.height and self.binary_a[y - 1][x - 1] == 9:
			while t_x - 1 > 0 and t_y - 1 > 0 and self.binary_a[t_y - 1][t_x - 1] == 9:
				t_x -= 1
				t_y -= 1
				count += 1
			t_y = y
			t_x = x
		# top left to right top
		if x + 1 < self.width and y + 1 < self.height and self.binary_a[y + 1][x + 1] == 9:
			while t_x + 1 < self.width and t_y + 1 < self.height and self.binary_a[t_y + 1][t_x + 1] == 9:
				t_x += 1
				t_y += 1
				count += 1
		if count == self.win_length - 1:
			print(x)  # win
			return 1
		return 0

	def is_defeat(self, y, x):
		t_y = y
		t_x = x
		count = 0
		# top to down
		if y + 1 < self.height and (self.binary_d[y + 1][x] == 8):
			# top
			while t_y + 1 < self.height and self.binary_d[t_y + 1][x] == 8:
				t_y += 1
				count += 1
		t_y = y
		t_x = x
		if count == self.win_length - 1:
			print(x)  # win
			return 1
		count = 0
		t_y = y
		t_x = x

		# right to left
		if x + 1 < self.width and self.binary_d[y][x + 1] == 8:
			# right
			while t_x + 1 < self.width and self.binary_d[y][t_x + 1] == 8:
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
		if count == self.win_length - 1:
			print(x)  # win
			return 1
		count = 0
		t_y = y
		t_x = x

		# left top to down right
		if x - 1 > 0 and y + 1 < self.height and self.binary_d[y + 1][x - 1] == 8:
			while t_x - 1 > 0 and t_y + 1 < self.height and self.binary_d[t_y + 1][t_x - 1] == 8:
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
		if count == self.win_length - 1:
			print(x)  # win
			return 1

		# right down to left down
		if x - 1 < self.width and y - 1 < self.height and self.binary_d[y - 1][x - 1] == 8:
			while t_x - 1 > 0 and t_y - 1 > 0 and self.binary_d[t_y - 1][t_x - 1] == 8:
				t_x -= 1
				t_y -= 1
				count += 1
			t_y = y
			t_x = x
		# top left to right top
		if x + 1 < self.width and y + 1 < self.height and self.binary_d[y + 1][x + 1] == 8:
			while t_x + 1 < self.width and t_y + 1 < self.height and self.binary_d[t_y + 1][t_x + 1] == 8:
				t_x += 1
				t_y += 1
				count += 1
		if count == self.win_length - 1:
			print(x)  # win
			return 1
		return 0

	def binary_mask(self, tab, target, target2):
		# Parcours le binary mask
		for y in range(0, self.height):
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
											# print('jecris sur la cell : ' + str(tab[j][x]))
											tab[j][x] = y - j
								break

					# Find right and project line to right
					for i in range(0, self.win_length):
						# Check for a O
						if x + i < self.width and tab[y][x + i] == target2:
							break

						# Fill with score start at x + win_length
						if x + i < self.width and tab[y][x + i] >= 0 and tab[y][x + i] <= 7:

							cell = False
							# Check above the cell
							if y == self.height - 1:
								cell = True
							elif y + 1 < self.height and x + i < self.width and (tab[y + 1][x + i] == 8 or tab[y + 1][x + i] == 9):
								cell = True

							# Project at x + i (right)
							if x + i < self.width and tab[y][x + i] >= 0 and tab[y][x + i] <= 7:
								if cell:
									# print('jecris sur la cell : ' + str(tab[y][x + i]))
									tab[y][x + i] = 1
								break

					# Find left and project line to left
					for i in range(0, self.win_length):
						# Check for a O
						if x - i >= 0 and tab[y][x - i] == target2:
							break

						# Fill with score start at x - win_length
						if x - i >= 0 and tab[y][x - i] >= 0 and tab[y][x - i] <= 7:
							cell = False
							# Check above the cell
							if y == self.height - 1:
								cell = True
							elif y + 1 < self.height and x - i >= 0 and (tab[y + 1][x - i] == 8 or tab[y + 1][x - i] == 9):
								cell = True

							# Project at x - i
							if x - i >= 0 and tab[y][x - i] >= 0 and tab[y][x - i] <= 7:
								#print('value de cell = ' + str(cell))
								if cell:
									tab[y][x - i] = 1
								break

							# # Project at x + win_length - 1
							# occurence = 0
							# for j in range(x - self.win_length + 1, x, 1):
							# 	if j >= 0 and tab[y][j] >= 0 and tab[y][j] <= 7:
							# 		occurence += 1

							# if occurence >= 1:
							# 	# Project at x + win_length - occurence
							# 	for j in range(x - occurence, x, 1):
							# 		if tab[y][j] != 9 and tab[y][j] != 8:
							# 			cost = self.find_cost_below_left(x - j, y, tab, x)
							# 			print('prix du cost = ' + str(cost))
							# 			if cost == 1:
							# 				if self.is_winning(y, j):
							# 					exit(1)
							# 				else:
							# 					tab[y][j] = cost
							# 	break
		return 1

	# Search for a winning point or a 1 defense

	def place_point(self):
		ones_ally = []
		ones_enemy = []
		# If the game start place a point in the middle
		if self.start == True:
			# self.binary_a[self.height - 1][int(self.width / 2)] = 9
			print(int(self.width / 2))
			self.put_in_tab(int(self.width / 2), 9)
			self.start = False

		# Find a winning point
		for y in range(0, self.height):
			for x in range(0, self.width):
				if self.binary_a[y][x] == 1:
					if self.is_winning(y, x) == 1:
						ones_enemy.append(x)
						exit(1)

		# Find winning enemy point
		for y in range(0, self.height):
			for x in range(0, self.width):
				if self.binary_d[y][x] == 1:
					ones_ally.append(x)
					if self.is_defeat(y, x) == 1:
						self.put_in_tab(x, 9)
						return

		# rand = random.randrange(0, len(ones_ally))
		# # Random choose for our points
		# for x in range(0, len(ones_ally)):
		# 	if x == rand:
		# 		print(x)
		# 		self.put_in_tab(int(x), 9)
		# 		return

		# rand = random.randrange(0, self.width)
		# # Random choose for their points
		# for x in range(0, self.width):
		# 	if x == rand:
		# 		print(x)
		# 		self.put_in_tab(int(x), 9)
		# 		return
		for y in range(0, self.height):
			for x in range(0, self.width):
				if self.binary_a[y][x] == 1:
					print(x)
					self.put_in_tab(int(x), 9)
					return