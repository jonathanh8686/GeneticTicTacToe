import random
class Random_AI():
    def __init__(self):
        pass
    
    def make_move(self, game):
        mr = (random.randint(0, game.BOARD_SIZE - 1))
        mc = (random.randint(0, game.BOARD_SIZE - 1))

        while (game.get_board()[mr][mc] != game.DEFAULT_LETTER):
            mr = (random.randint(0, game.BOARD_SIZE-1))
            mc = (random.randint(0, game.BOARD_SIZE-1))

        return (mr, mc)
    
    def breed(self, other, mutation_factor):
        # there is no point in breeding random ais
        return self

