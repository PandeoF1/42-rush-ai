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
    game_status = 0
    t_time = 10000
    g_time = 100

    # TODO :
    #   . Creation of tab

    tab = 0

    game = Game(tab, height, width, win_length, t_time, g_time, game_status)

    while game.game_status:
        test = input
        print(test)


if __name__ == "__main__":
    main()
