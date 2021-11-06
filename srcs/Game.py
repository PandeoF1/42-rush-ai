import sys


class Game(object):

    # TODO : game params
    def __init__(self, height, width, win_length, t_time, g_time, game_status):
        self.height = height
        self.width = width
        self.win_length = win_length
        self.t_time = t_time # Total time
        self.g_time = g_time # Gain time per round
        self.game_status = game_status # 1 = in progress / 0 = finish
        self.tab = self.create_tab()

    def status(self):
        return (self.game_status)

    def create_tab(self):
        tab = []
        h = 0
        w = 0
        while (h < self.height):
            h += 1
            while (w < self.width):
                tab[h][w] = 0
                w += 1
            w = 0
        return (tab)

    def show_tab(self):
        self.tab = []
        h = 0
        w = 0
        while (h < self.height):
            h += 1
            while (w < self.width):
                print(self.tab[h][w])
                w += 1
            w = 0
        return (1)


    def basic_func(self, val):
        print("je suis une function " + str(val))
        return 1
