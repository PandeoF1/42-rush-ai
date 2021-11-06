from Game import Game
import sys
import os
import time
import psutil as ps

#while (True):
#	data = input()
#	f = open("test.txt", "a")
#	f.write(data)
#	f.close()

# Basic printer, used to say which column we played
def printer(value):
	print(value)


# Main function
def main():
	print(str(os.getpid())+ "\n", file=sys.stderr)
	# = open("log.txt", "a")
	# width = input()
	# f.write("Input width : " + str(width))
	# height = input()
	# f.write("Input height : " + str(height))
	# win_length = input()
	# f.write("Input win_length : " + str(win_length))
	# play_order = input()
	# f.write("Input play_order : " + str(play_order))
	# game_status = 1
	# g_time = input()
	# f.write("Input g_time : " + str(g_time))
	# t_time = input()
	# f.write("Input t_time : " + str(t_time))
	# f.close()
	width = 10
	height = 10
	win_length = 4
	play_order = 2
	game_status = 1
	g_time = 100000
	t_time = 1000
	# TODO :
	#   . Creation of tab

	game = Game(height, width, win_length, g_time, t_time, game_status)
	game.create_tab()
	game.create_tab_binary()
	while game.game_status:
		with open('/Users/hosra/Desktop/42/42-rush-ai/srcs/status.txt') as file: # Force quit
			first_line = file.readline() # Force quit
		if first_line == "1": # Force quit
			exit(1) # Force quit

		if play_order == 2:
			x = input()
		else:
			x = 0
		game.put_in_tab(int(x), int(play_order))
		
		game.binary_mask()
		game.show_tab_binary()
		time.sleep(int(t_time) / 1000)
		

if __name__ == "__main__":
	main()
