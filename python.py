import numpy as np
import random
from scipy import stats
import matplotlib.pyplot as pltgit 
# import pygame

# pygame.init()

# # Fullscreen
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# pygame.display.set_caption("Tetris")
# clock = pygame.time.Clock()

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:  # ESC to exit fullscreen
#                 running = False

#     screen.fill((0, 0, 0))
#     pygame.display.flip()
#     clock.tick(60)

# pygame.quit()

# class Piece:
#     def __init__(self, shape):
#         self.shape = shape          # список списков (матрица фигуры)
#         self.x = 0
#         self.y = 0
#         self.rotation = 0

# # Твои фигуры в списке
# figures = [
#     Piece([[1, 1, 1, 1]]),                    # I горизонтальная
#     Piece([[1, 1], [1, 1]]),                  # O
#     Piece([[0, 1, 0], [1, 1, 1]]),            # T
#     # ... твои остальные
# ]

# # Пример использования
# current_piece = figures[0]
# current_piece.x = 5
# current_piece.y = 0
# current_piece.rotation = 1

class Piece:
    def __init__(self, shape):
        self.shape = shape      # список списков (матрица фигуры)
        self.x = 0
        self.y = 0
        self.rotation = 0


# Пример как создавать фигуры:
I = Piece([[1, 1, 1, 1]])

II = Piece([[1, 0, 0],
            [1, 0, 0], 
            [1, 0, 0],
            [1, 0, 0]])

O = Piece([[1, 1],
           [1, 1]])

T = Piece([[0, 1, 0],
           [1, 1, 1]])

TT = Piece([[1, 1, 1],
            [0, 1, 0]])

TTT = Piece([[1, 0, 0],
             [1, 1, 0],
             [1, 0, 0]])

TTTT = Piece([[0, 0, 1],
              [0, 1, 1],
              [0, 0, 1]])

J = Piece([[1, 0, 0],
           [1, 1, 1]])

JJ = Piece([[0, 0, 1],
            [0, 0, 1],
            [0, 1, 1]])

JJJ = Piece([[1, 1, 1],
             [0, 0, 1],
             [0, 0, 0]])

JJJJ = Piece([[1, 1, 0],
              [1, 0, 0],
              [1, 0, 0]])

L = Piece([[1, 0, 0],
           [1, 0, 0],
           [1, 1, 0]])

LL = Piece([[0, 0, 1],
            [1, 1, 1]])

LLL = Piece([[0, 1, 1],
             [0, 0, 1],
             [0, 0, 1]])

LLLL = Piece([[1, 1, 1],
              [1, 0, 0],
              [0, 0, 0]])

S = Piece([[0, 1, 1],
           [1, 1, 0]])

SS = Piece([[1, 1, 0],
            [0, 1, 1]])

SSS = Piece([[0, 1, 0],
             [1, 1, 0], 
             [1, 0, 0]])

SSSS = Piece([[1, 0, 0],
              [1, 1, 0], 
              [0, 1, 0]])

# и т.д.

LOOT_TABLE = [
    {"name": I,     "probability": 0.55, "score_deal": 200},
    {"name": II,    "probability": 0.05, "score_deal": 200},
    {"name": O,     "probability": 0.25, "score_deal": 200},
    {"name": T,     "probability": 0.15, "score_deal": 200},
    {"name": TT,    "probability": 0.15, "score_deal": 200},
    {"name": TTT,   "probability": 0.15, "score_deal": 200},
    {"name": TTTT,  "probability": 0.15, "score_deal": 200},
    {"name": J,     "probability": 0.05, "score_deal": 200},
    {"name": JJ,    "probability": 0.05, "score_deal": 200},
    {"name": JJJ,   "probability": 0.05, "score_deal": 200},
    {"name": JJJJ,  "probability": 0.05, "score_deal": 200},
    {"name": L,     "probability": 0.05, "score_deal": 200},
    {"name": LL,    "probability": 0.05, "score_deal": 200},
    {"name": LLL,   "probability": 0.05, "score_deal": 200},
    {"name": LLLL,  "probability": 0.05, "score_deal": 200},
    {"name": S,     "probability": 0.05, "score_deal": 200},
    {"name": SS,    "probability": 0.05, "score_deal": 200},
    {"name": SSS,   "probability": 0.05, "score_deal": 200},
    {"name": SSSS,  "probability": 0.05, "score_deal": 200},
]

total = sum(item["probability"] for item in LOOT_TABLE)
print(f"Probabilities sum to: {total}")

def single_loot_drop(loot_table):
    """
    Simulates opening one loot chest.
    Returns the dropped item (a dictionary).
    """
    roll = random.random()
    cumulative = 0.0

    for item in loot_table:
        cumulative += item["probability"]
        if roll < cumulative:
            return item
            pass

    return loot_table[-1]  # fallback


# Test your function by running this here
drop = single_loot_drop(LOOT_TABLE)

def run_simulation(loot_table, num_trials=10_000):
    """
    Runs num_trials loot drops and returns the results.

    Returns:
        results     - list of item names (strings)
        gold_earned - list of gold values (ints)
    """
    results = []
    gold_earned = []

    for _ in range(num_trials):
        item = single_loot_drop(loot_table)
        results.append(item["name"])
        gold_earned.append(item["score_deal"])
        pass

    return results, gold_earned


random.seed(random.randint(1, 1000000))
results, gold_earned = run_simulation(LOOT_TABLE, 10_000)
print(results[:3])
