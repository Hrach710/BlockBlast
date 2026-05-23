import numpy as np
import random
import pygame
from scipy import stats
import matplotlib.pyplot as pltgit
# import traceback

# try:
#     show_in_window(all_pieces)
# except Exception as e:
#     traceback.print_exc()
#     input("Ошибка! Нажми Enter...")

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

def show_in_window(my_pieces):
    """my_pieces = список твоих объектов Piece"""
    import pygame
    import random
    import sys

    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    clock = pygame.time.Clock()
    BLOCK_SIZE = 40
    GRID_X, GRID_Y = 120, 80
    grid = [[None for _ in range(8)] for _ in range(8)]  # 8x8 grid

    class VisualPiece:
        def __init__(self, piece):
            self.piece = piece
            self.color = random.choice([(0,255,255),(255,255,0),(128,0,128),(0,0,255),(255,165,0),(0,255,0)])
            self.dragging = False
            self.offset_x = 0
            self.offset_y = 0

        def draw(self, surface, ox=0, oy=0):
            for y, row in enumerate(self.piece.shape):
                for x, cell in enumerate(row):
                    if cell:
                        pygame.draw.rect(surface, self.color, 
                                       (ox + x*BLOCK_SIZE, oy + y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                        pygame.draw.rect(surface, (255,255,255), 
                                       (ox + x*BLOCK_SIZE, oy + y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 3)
                        

    def get_grid_pos(mouse):
        gx = (mouse[0] - GRID_X) // BLOCK_SIZE
        gy = (mouse[1] - GRID_Y) // BLOCK_SIZE
        return gx, gy
        
    def can_place(piece, gx, gy):
        for y, row in enumerate(piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    nx, ny = gx+x, gy+y
                    if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
                        return False
                    if grid[ny][nx] is not None:
                        return False
        return True

    def place_piece(piece, gx, gy):
        for y, row in enumerate(piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    grid[gy+y][gx+x] = piece
                        


    preview_pos = [(130,560), (450,560), (700,560)]
    selected = None

    def generate_new_three():
        return [VisualPiece(random.choice(my_pieces)) for _ in range(3)]
    
    visuals = generate_new_three() # 3 фигуры внизу

    running = True
    while running:
        mouse = pygame.mouse.get_pos()
        drag_x = mouse[0] - selected.offset_x if selected else mouse[0]
        drag_y = mouse[1] - selected.offset_y if selected else mouse[1]
        gx, gy = get_grid_pos((drag_x, drag_y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, v in enumerate(visuals):
                    px, py = preview_pos[i]
                    if px-40 < mouse[0] < px+160 and py-40 < mouse[1] < py+160:
                        selected = v
                        selected.dragging = True
                        selected.offset_x = mouse[0] - px
                        selected.offset_y = mouse[1] - py

            if event.type == pygame.MOUSEBUTTONUP:
                if selected:
                    if can_place(selected.piece, gx, gy):
                        place_piece(selected.piece, gx, gy)
                        visuals = [v for v in visuals if v != selected]  # убираем из превью
                        if len(visuals) == 0:
                            visuals = generate_new_three()
                    selected.dragging = False
                    selected = None

        screen.fill((0,0,0))

        # 8x8 grid
        for x in range(8):
            for y in range(8):
                pygame.draw.rect(screen, (45,45,45), 
                               (GRID_X + x*BLOCK_SIZE, GRID_Y + y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)
                
        for y in range(8):
            for x in range(8):
                if grid[y][x] is not None:
                    pygame.draw.rect(screen, (100,100,255), 
                                   (GRID_X + x*BLOCK_SIZE, GRID_Y + y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(screen, (255,255,255), 
                                   (GRID_X + x*BLOCK_SIZE, GRID_Y + y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 3)
                    
        if selected and selected.dragging and can_place(selected.piece, gx, gy):
            for y, row in enumerate(selected.piece.shape):
                for x, cell in enumerate(row):
                    if cell:
                        px  = GRID_X + (gx+x)*BLOCK_SIZE
                        py  = GRID_Y + (gy+y)*BLOCK_SIZE
                        c = selected.color
                        shadow = (c[0]//2, c[1]//2, c[2]//2)
                        pygame.draw.rect(screen, shadow, (px, py, BLOCK_SIZE, BLOCK_SIZE))
                        pygame.draw.rect(screen, (255,255,255), (px, py, BLOCK_SIZE, BLOCK_SIZE), 3)

        # 3 фигуры внизу
        for i, v in enumerate(visuals[:3]):
            if v != selected:  # не рисуем ту, что тащим
                v.draw(screen, preview_pos[i][0], preview_pos[i][1])

        # dragging
        if selected and selected.dragging:
            selected.draw(screen, mouse[0]-selected.offset_x, mouse[1]-selected.offset_y)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

# После всех твоих объектов (I, II, O, T ...)
all_pieces = [I, II, O, T, TT, TTT, TTTT, J, JJ, JJJ, JJJJ, L, LL, LLL, LLLL, S, SS, SSS, SSSS]  # добавь все

show_in_window(all_pieces)

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