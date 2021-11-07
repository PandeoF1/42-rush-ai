#!/usr/bin/env python3

from Game import Game
import sys
import os
import time


# Main function
def main():
        
	print(str(os.getpid())+ "\n", file=sys.stderr)
	f = open("log.txt", "w")
	if len(sys.argv) == 2:
		width = 7
		height = 6
		win_length = 4
		play_order = 1
		game_status = 1
		g_time = 100000
		t_time = 1000
	else:
		width = input()
		f.write("Input width : " + str(width)+ '\n')
		height = input()
		f.write("Input height : " + str(height)+ '\n')
		win_length = input()
		f.write("Input win_length : " + str(win_length)+ '\n')
		play_order = input()
		f.write("Input play_order : " + str(play_order)+ '\n')
		game_status = 1
		g_time = input()
		f.write("Input g_time : " + str(g_time)+ '\n')
		t_time = input()
		f.write("Input t_time : " + str(t_time) + '\n')
	# f.close()
	# TODO :
	#   . Creation of tab

	game = Game(height, width, win_length, g_time, t_time, game_status)
	# game.create_tab()
	# game.create_tab_binary()
	f = open("log.txt", "a")
	while game.game_status:
		with open('status.txt') as file: # Force quit
			first_line = file.readline() # Force quit
		if first_line == "1": # Force quit
			exit(1) # Force quit
		x = -42
		
		if play_order == '2':
			try:
				x = input()
				if (x == ''):
					x = input()
			except EOFError:
				f.close()
				return	
		if x != -42:
			f.write("(" + str(play_order) + ") Player input : " + str(x)+ '\n')
		else:
			f.write("(" + str(play_order) + ") Notre tours :)\n")
		if play_order == '2' and int(x) <= game.height - 1:
			game.put_in_tab(int(x), 8)
			game.binary_mask(game.binary_d, 8, 9)
		if play_order == '1':
			game.place_point()
		game.binary_mask(game.binary_a, 9, 8)
		if len(sys.argv) == 2:
			game.show_tab_binary()
		# game.show_tab()
		#if int(t_time) >= 1:
		#	time.sleep(int(t_time) / 1000)

		if play_order == '2':
			play_order = '1'
		else:
			play_order = '2'
	f.close()

if __name__ == "__main__":
	main()
