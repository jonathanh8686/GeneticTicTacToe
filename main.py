from blind_ai import Blind_AI
import random
from game import Game
import matplotlib.pyplot as plt
from random_ai import Random_AI
import os
import time
cls = lambda: os.system('cls')

def generate_blind_ais(n):
    rtn = []
    for i in range(n):
        rtn.append(Blind_AI())
    return rtn

def generate_random_ais(n):
    return [Random_AI() for _ in range(n)]

def get_winner(ai1, ai2):
    g = Game()
    active_player = ai1
    while(g.in_progress()):
        g.make_move(*active_player.make_move(g))
        active_player = ai2 if active_player == ai1 else ai1
    if(g.check_won() == "X"):
        return ai1
    elif(g.check_won() == "O"):
        return ai2
    return random.choice([ai1, ai2])

def get_winners(ais):
    winners = []
    for i in range(0, 2*(len(ais)//2), 2):
        winners.append(get_winner(ais[i], ais[i+1]))
    return winners


def get_individual_fitness(ai, runs):
    wins = 0
    for _ in range(runs):
        if(get_winner(ai, Random_AI()) == ai):
            wins += 1
    return wins / runs

def get_pool_fitness(pop_size, generations, ai_kind):
    fitness = []
    pool = []
    if(ai_kind == "random"):
        pool = [Random_AI() for _ in range(pop_size)]
    elif(ai_kind == "blind"):
        pool = [Blind_AI() for _ in range(pop_size)]

    for i in range(generations):
        total_fitness = 0
        for ai in pool:
            total_fitness += get_individual_fitness(ai, 10)
        fitness.append(total_fitness / len(pool))
        print(f"Processing generation {i} -- Fitness: {total_fitness/len(pool)}")

        while(len(pool) > 2):
            pool = get_winners(pool)
        while(len(pool) < 256):
            pool.append(pool[0].breed(pool[1], 0))

    return fitness

def main():
    plt.plot(get_pool_fitness(256, 10, "random"))
    plt.plot(get_pool_fitness(256, 10, "blind"))
    plt.show()

if __name__ == "__main__":
    main()

    # g = Game()
    # active_player = pool[0]
    # while(g.in_progress()):
    #     g.make_move(*active_player.make_move(g))
    #     active_player = pool[1] if active_player == pool[0] else pool[0]
    #     cls()
    #     print(g)
    #     time.sleep(0.3)

    # g = Game()
    # while(g.in_progress()):
    #     mv = input().strip().split(" ")
    #     g.make_move(int(mv[0]), int(mv[1]))
    #     if(g.check_won()):
    #         break
    #     mv = finalAI.make_move(g)
    #     g.make_move(int(mv[0]), int(mv[1]))
    #     print(g)
    
    # print(g.check_won() + " won!")