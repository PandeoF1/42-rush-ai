from Game import Game


# Basic printer, used to say which column we played
def printer(value):
	print(value)


# Main function
def main():
	width = input()
	height = input()
	win_length = input()
	play_order = input()
	game_status = 1
	t_time = 10000
	g_time = 100

	# TODO :
	#   . Creation of tab

	game = Game(height, width, win_length, t_time, g_time, game_status)
	game.show_tab()

	while game.game_status:
		a = input()
		b = input()
		game.put_in_tab(a, b, 1)
		game.show_tab()
		a = input()
		b = input()
		game.put_in_tab(a, b, 2)
		game.show_tab()



if __name__ == "__main__":
	main()
