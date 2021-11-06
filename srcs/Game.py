import sys


class Game(object):

	# TODO : game params
	def __init__(self, height, width, win_length, t_time, g_time, game_status):
		self.height = int(height)
		self.width = int(width)
		self.win_length = int(win_length)
		self.t_time = int(t_time) # Total time
		self.g_time = int(g_time) # Gain time per round
		self.game_status = int(game_status) # 0 = in progress / 1 = finish
		self.tab = self.create_tab()

	def status(self):
		return (self.game_status)

	def create_tab(self):
		tab = []
		
		for _ in range(0, self.height):
			line = [0] * self.width
			tab.append(line)

		return (tab)

	def show_tab(self):
		for i in range(0, self.height):
			print(self.tab[i])

	def put_in_tab(self, height, width, player):
		self.tab[int(height)][int(width)] = int(player)

	def basic_func(self, val):
		print("je suis une function " + str(val))
		return 1
