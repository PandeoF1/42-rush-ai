import sys


class Game(object):

    # TODO : game params
    def __init__(self, tab, height, width, win_length, t_time, g_time, game_status):
        self.tab = tab
        self.height = height
        self.width = width
        self.win_length = win_length
        self.t_time = t_time # Total time
        self.g_time = g_time # Gain time per round
        self.game_status = game_status # 1 = in progress / 0 = finish

    def game_status(self):
        return (self.game_status)

    def basic_func(self, val):
        print("je suis une function " + str(val))
        return 1
