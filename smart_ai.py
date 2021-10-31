import random

class Smart_AI(object):
    def __init__(self, board_size=3, strat=[]):
        self.strategy = []
        if(strat != []):
            self.strategy = strat
        else:
            move_options = []
            for i in range(board_size):
                for j in range(board_size):
                    move_options.append((i, j))
                
            for i in range(board_size):
                for j in range(board_size):
                    random.shuffle(move_options)
                    self.strategy.append(move_options[:])

            random.shuffle(self.strategy)
    
    def make_move(self, game):
        mc = sum([sum([i != game.DEFAULT_LETTER for i in j]) for j in game.get_board()]) - 1
        brd = game.get_board()
        i = 0
        candidate = self.strategy[mc][i]
        while(brd[candidate[0]][candidate[1]] != game.DEFAULT_LETTER):
            i = (i + 1) % len(self.strategy[mc])
            candidate = self.strategy[mc][i]
        return candidate

    def breed(self, other, mutation_factor):
        child_strategy = []

        for i in range(len(self.strategy)):
            mutation_roll = random.random()
            if(mutation_roll <= mutation_factor):
                mutated_strat = self.strategy[len(child_strategy)][:]
                random.shuffle(mutated_strat)
                child_strategy.append(mutated_strat)
                continue

            roll = random.randint(0, 1)
            if(roll == 0):
                child_strategy.append(self.strategy[len(child_strategy)][:])
            else:
                child_strategy.append(other.strategy[len(child_strategy)][:])
        
        return Blind_AI(strat=child_strategy)


