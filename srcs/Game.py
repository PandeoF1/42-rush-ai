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

	def put_in_tab(self, width, player): # DONE
		n = 0
		while self.tab[n][width] == 0 and n < self.height - 1:
			n += 1
			print(str(n) + "\n")
		if self.tab[n][width] != 0:
			n -= 1
		self.tab[n][width] = player
		if n > self.max_height:
			self.max_height = n
	



	
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

# 	# Try to find an occurence with winning length
# 	def find_end_occurence(self, x, y):
# 		occurence = []

# 		start = 0
# 		end = 0
# 		orentation = 'E'

# 		# Check length of potential occurence
# 		if self.height - y < self.win_length:
# 			return -1
# ]
# 		# Right search
# 		for i in range(0, self.win_length):
# 			if 

# 		return 0