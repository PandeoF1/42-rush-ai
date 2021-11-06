import sys
from Game import Game

width = input()
height = input()
win_length = input()
play_order = input()
game_status = 0;
t_time = 10000
g_time = 100

# TODO : 
#   . Creation of tab

game = Game(height, width, win_length, t_time, g_time, game_status)

while (game.status):
	test = input
	game.show_tab()
	print(test)