import sys


class Game(object):

    # TODO : game params
    def __init__(self, size):
        self.size = size


    def basic_func(self, val):
        print("je suis une function " + str(val))
        return 1


game = Game(size=1000)
game.basic_func(42)