from random import random
from unittest import result
import random
import math

class Piece:
    def __init__(self, shape):
        self.shape = shape
        self.x = 0
        self.y = 0
        self.rotation = 0

G = Piece([[0, 0, 0],
           [0, 1, 0],
           [0, 0, 0]])

GG = Piece([[0, 0, 0],
            [0, 1, 0],
            [0, 1, 0]])

GGG = Piece([[1, 1, 0]])

GGGG = Piece([[0, 1, 0],
              [1, 1, 0]])

GGGGG = Piece([[1, 0, 0],
               [1, 1, 0]])

GGGGGG = Piece([[1, 1, 0],
                [0, 1, 0]])

GGGGGGG = Piece([[0, 1, 1],
                 [0, 1, 0]])

I = Piece([[1, 1, 1, 1]])

II = Piece([[1, 0, 0],
            [1, 0, 0],
            [1, 0, 0],
            [1, 0, 0]])

III = Piece([[1, 1, 1, 1]])

IIII = Piece([[0, 1, 0],
              [0, 1, 0],
              [0, 1, 0],
              [0, 1, 0]])

IIIII = Piece([[0, 1, 0],
               [0, 1, 0],
               [0, 1, 0],
               [0, 1, 0],
               [0, 1, 0]])

IIIIII = Piece([[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]])

IIIIIII = Piece([[0, 1, 0],
                 [0, 1, 0],
                 [0, 1, 0],
                 [0, 0, 0]])

IIIIIIII = Piece([[0, 0, 0],
                  [1, 1, 1],
                  [0, 0, 0]])

O = Piece([[1, 1],
           [1, 1]])

OO = Piece([[1, 1, 0],
            [1, 1, 0],
            [1, 1, 0]])

OOO = Piece([[0, 0, 0],
             [1, 1, 1],
             [1, 1, 1]])

OOOO = Piece([[1, 1, 1],
              [1, 1, 1],
              [1, 1, 1]])

T = Piece([[0, 1, 0],
           [1, 1, 1]])

TT = Piece([[1, 1, 1],
            [0, 1, 0]])

TTT = Piece([[0, 1, 0],
             [0, 1, 1],
             [0, 1, 0]])

TTTT = Piece([[0, 1, 0],
              [1, 1, 0],
              [0, 1, 0]])

J = Piece([[1, 0, 0],
           [1, 1, 1]])

JJ = Piece([[0, 1, 0],
            [0, 1, 0],
            [1, 1, 0]])

JJJ = Piece([[0, 0, 0],
             [1, 1, 1],
             [0, 0, 1]])

JJJJ = Piece([[0, 1, 1],
              [0, 1, 0],
              [0, 1, 0]])

L = Piece([[0, 1, 0],
           [0, 1, 0],
           [0, 1, 1]])

LL = Piece([[0, 0, 1],
            [1, 1, 1]])

LLL = Piece([[1, 1, 0],
             [0, 1, 0],
             [0, 1, 0]])

LLLL = Piece([[0, 0, 0],
              [1, 1, 1],
              [1, 0, 0]])

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

LOOT_TABLE = [
    {"name": G,    "probability": (1.00/34), "score_deal": random.randint(50, 400)},
    {"name": GG,   "probability": (1.00/34), "score_deal": random.randint(50, 400)},
    {"name": GGG,  "probability": (1.00/34), "score_deal": random.randint(50, 400)},
    {"name": GGGG, "probability": (1.00/34), "score_deal": random.randint(50, 400)},
    {"name": GGGGG, "probability": (1.00/34), "score_deal": random.randint(50, 400)},
    {"name": GGGGGG, "probability": (1.00/34), "score_deal": random.randint(50, 400)},
    {"name": GGGGGGG, "probability": (1.00/34), "score_deal": random.randint(50, 400)},
    {"name": I,     "probability": (1.00/34), "score_deal": random.randint(50, 400)},
    {"name": II,    "probability": (1.00/34), "score_deal": random.randint(50, 400)},
    {"name": III,   "probability": (1.00/34), "score_deal": random.randint(50, 400)},
    {"name": IIII,  "probability": (1.00/34), "score_deal": random.randint(50, 400)},
    {"name": IIIII, "probability": (1.00/34), "score_deal": random.randint(50, 400)},
    {"name": IIIIII, "probability": (1.00/34), "score_deal": random.randint(50, 400)},
    {"name": IIIIIII, "probability": (1.00/34), "score_deal": random.randint(50, 400)},
    {"name": IIIIIIII, "probability": (1.00/34), "score_deal": random.randint(50, 400)},
    {"name": O,     "probability": (1.00/34), "score_deal": random.randint(50, 400)},
    {"name": OO,    "probability": (1.00/34), "score_deal": random.randint(50, 400)},
    {"name": OOO,   "probability": (1.00/34), "score_deal": random.randint(50, 400)},
    {"name": OOOO,  "probability": (1.00/34), "score_deal": random.randint(50, 400)},
    {"name": T,     "probability": (1.00/34), "score_deal": random.randint(50, 400)},
    {"name": TT,    "probability": (1.00/34), "score_deal": random.randint(50, 400)},
    {"name": TTT,   "probability": (1.00/34), "score_deal": random.randint(50, 400)},
    {"name": TTTT,  "probability": (1.00/34), "score_deal": random.randint(50, 400)},
    {"name": J,     "probability": (1.00/34), "score_deal": random.randint(50, 400)},
    {"name": JJ,    "probability": (1.00/34), "score_deal": random.randint(50, 400)},
    {"name": JJJ,   "probability": (1.00/34), "score_deal": random.randint(50, 400)},
    {"name": JJJJ,  "probability": (1.00/34), "score_deal": random.randint(50, 400)},
    {"name": L,     "probability": (1.00/34), "score_deal": random.randint(50, 400)},
    {"name": LL,    "probability": (1.00/34), "score_deal": random.randint(50, 400)},
    {"name": LLL,   "probability": (1.00/34), "score_deal": random.randint(50, 400)},
    {"name": LLLL,  "probability": (1.00/34), "score_deal": random.randint(50, 400)},
    {"name": S,     "probability": (1.00/34), "score_deal": random.randint(50, 400)},
    {"name": SS,    "probability": (1.00/34), "score_deal": random.randint(50, 400)},
    {"name": SSS,   "probability": (1.00/34), "score_deal": random.randint(50, 400)},
    {"name": SSSS,  "probability": (1.00/34), "score_deal": random.randint(50, 400)},
]

def show_in_window(my_pieces, loot_table):
    import pygame
    import random
    import sys

    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    clock = pygame.time.Clock()
    BLOCK_SIZE = 40
    GRID_X = (1000 - 8 * BLOCK_SIZE) // 2
    GRID_Y = 150
    grid = [[None for _ in range(8)] for _ in range(8)]
    score = 0
    game_over =  False
    display_score = 0
    animations = []
    particles = []

    class VisualPiece:
        def __init__(self, piece):
            self.score_deal = 0
            self.piece = piece
            self.color = random.choice([(0,255,255),(255,255,0),(128,0,128),(0,0,255),(255,165,0),(0,255,0)])
            self.dragging = False
            self.offset_x = 0
            self.offset_y = 0

        def draw(self, surface, ox=0, oy=0):
            for y, row in enumerate(self.piece.shape):
                for x, cell in enumerate(row):
                    if cell:
                        bx = ox + x*BLOCK_SIZE
                        by = oy + y*BLOCK_SIZE
                        pygame.draw.rect(surface, self.color, (bx, by, BLOCK_SIZE, BLOCK_SIZE))
                        dark = (max(0,self.color[0]-80), max(0,self.color[1]-80), max(0,self.color[2]-80))
                        pygame.draw.rect(surface, dark, (bx, by + BLOCK_SIZE - 6, BLOCK_SIZE - 6, 6))
                        pygame.draw.rect(surface, dark, (bx + BLOCK_SIZE - 6, by, 6, BLOCK_SIZE))
                        light = (min(255,self.color[0]+100), min(255,self.color[1]+100), min(255,self.color[2]+100))
                        pygame.draw.rect(surface, light, (bx, by, BLOCK_SIZE, 6))
                        pygame.draw.rect(surface, light, (bx, by, 6, BLOCK_SIZE))
                        inner = (max(0, min(255, self.color[0]-30)), max(0, min(255, self.color[1]-30)), max(0, min(255, self.color[2]-30)))
                        pygame.draw.rect(surface, inner, (bx + 5, by + 5, BLOCK_SIZE - 11, BLOCK_SIZE - 11))

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

    def check_game_over(current_visuals):
        for v in current_visuals:
            if v is None:
                continue
            for gy in range(8):
                for gx in range(8):
                    if can_place(v.piece, gx, gy):
                        return False
        return True

    def place_piece(piece, gx, gy, color=(255,255,255), score_deal=200):
        nonlocal score
        for y, row in enumerate(piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    grid[gy+y][gx+x] = color
        score += score_deal

    def clear_and_check_lines():
        nonlocal score
        lines_cleared = 0
        cells_to_clear = set()

        for y in range(8):
            if all(grid[y][x] is not None for x in range(8)):
                for x in range(8):
                    cells_to_clear.add((x, y))
                lines_cleared += 1

        for x in range(8):
            if all(grid[y][x] is not None for y in range(8)):
                for y in range(8):
                    cells_to_clear.add((x, y))
                lines_cleared += 1

        for (x, y) in cells_to_clear:
            color = grid[y][x]
            grid[y][x] = None
            cx = GRID_X + x * BLOCK_SIZE + BLOCK_SIZE // 2
            cy = GRID_Y + y * BLOCK_SIZE + BLOCK_SIZE // 2
            for _ in range(12):
                angle = random.uniform(0, 2 * math.pi)
                speed = random.uniform(2, 8)
                particles.append({
                    "x": float(cx),
                    "y": float(cy),
                    "vx": speed * math.cos(angle),
                    "vy": speed * math.sin(angle),
                    "color": color,
                    "size": random.randint(5, 12),
                    "life": random.randint(25, 50),
                    "max_life": 50,
                })

        if lines_cleared > 0:
            bonus = lines_cleared * 200
            score += bonus
            animations.append({
                "text": f"+{bonus} CLEAR x{lines_cleared}",
                "x": GRID_X,
                "y": GRID_Y - 30,
                "alpha": 255,
                "timer": 90
            })

    preview_pos = [(130,560), (450,560), (700,560)]
    selected = None

    def generate_new_three():
        choice = random.choices(loot_table, weights=[item["probability"] for item in loot_table], k=3)
        result = []
        for item in choice:
            vp = VisualPiece(item["name"])
            vp.score_deal = item["score_deal"]
            result.append(vp)
        return result

    visuals = generate_new_three()
    font = pygame.font.SysFont(None, 48)
    running = True

    while running:
        mouse = pygame.mouse.get_pos()
        drag_x = mouse[0] - selected.offset_x if selected else mouse[0]
        drag_y = mouse[1] - selected.offset_y if selected else mouse[1]
        gx, gy = get_grid_pos((drag_x, drag_y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not game_over:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, v in enumerate(visuals):
                    if v is None:
                        continue
                    px, py = preview_pos[i]
                    if px-40 < mouse[0] < px+160 and py-40 < mouse[1] < py+160:
                        selected = v
                        selected.dragging = True
                        selected.offset_x = mouse[0] - px
                        selected.offset_y = mouse[1] - py

            if event.type == pygame.MOUSEBUTTONUP:
                if selected:
                    if can_place(selected.piece, gx, gy):
                        place_piece(selected.piece, gx, gy, selected.color, selected.score_deal)
                        clear_and_check_lines()
                        animations.append({
                            "text": f"+{selected.score_deal}",
                            "x": GRID_X + gx*BLOCK_SIZE,
                            "y": GRID_Y + gy*BLOCK_SIZE,
                            "alpha": 255,
                            "timer": 60
                        })
                        idx = visuals.index(selected)
                        visuals[idx] = None
                        if all(v is None for v in visuals):
                            visuals = generate_new_three()
                        if check_game_over(visuals):
                            game_over = True

                    selected.dragging = False
                    selected = None

        screen.fill((0, 0, 0))

        if display_score < score:
            display_score += 5
        score_text = font.render(f"Score: {display_score}", True, (255,255,255))
        screen.blit(score_text, (GRID_X, GRID_Y - 60))

        for anim in animations[:]:
            anim["y"] -= 2
            anim["timer"] -= 1
            anim["alpha"] = int(255 * anim["timer"] / 60)
            anim_surf = font.render(anim["text"], True, (255,255,0))
            anim_surf.set_alpha(anim["alpha"])
            screen.blit(anim_surf, (anim["x"], anim["y"]))
            if anim["timer"] <= 0:
                animations.remove(anim)

        # Grid lines
        for x in range(8):
            for y in range(8):
                pygame.draw.rect(screen, (45,45,45),
                                 (GRID_X + x*BLOCK_SIZE, GRID_Y + y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

        # Grid blocks
        for x in range(8):
            for y in range(8):
                if grid[y][x] is not None:
                    color = grid[y][x]
                    bx = GRID_X + x*BLOCK_SIZE
                    by = GRID_Y + y*BLOCK_SIZE
                    pygame.draw.rect(screen, color, (bx, by, BLOCK_SIZE, BLOCK_SIZE))
                    dark = (max(0,color[0]-80), max(0,color[1]-80), max(0,color[2]-80))
                    pygame.draw.rect(screen, dark, (bx, by + BLOCK_SIZE - 6, BLOCK_SIZE - 6, 6))
                    pygame.draw.rect(screen, dark, (bx + BLOCK_SIZE - 6, by, 6, BLOCK_SIZE))
                    light = (min(255,color[0]+100), min(255,color[1]+100), min(255,color[2]+100))
                    pygame.draw.rect(screen, light, (bx, by, BLOCK_SIZE, 6))
                    pygame.draw.rect(screen, light, (bx, by, 6, BLOCK_SIZE))
                    inner = (max(0, min(255, color[0]-30)), max(0, min(255, color[1]-30)), max(0, min(255, color[2]-30)))
                    pygame.draw.rect(screen, inner, (bx + 5, by + 5, BLOCK_SIZE - 11, BLOCK_SIZE - 11))

        # --- ЧАСТИЦЫ --- рисуем здесь, после сетки
        for p in particles[:]:
            p["x"] += p["vx"]
            p["y"] += p["vy"]
            p["vy"] += 0.3  # гравитация
            p["life"] -= 1
            alpha_ratio = p["life"] / p["max_life"]
            size = max(1, int(p["size"] * alpha_ratio))
            c = p["color"]
            bright = (min(255, c[0]+80), min(255, c[1]+80), min(255, c[2]+80))
            surf = pygame.Surface((size, size), pygame.SRCALPHA)
            surf.fill((*bright, int(255 * alpha_ratio)))
            screen.blit(surf, (int(p["x"]), int(p["y"])))
            if p["life"] <= 0:
                particles.remove(p)

        # Ghost placement
        if selected and selected.dragging and can_place(selected.piece, gx, gy):
            for y, row in enumerate(selected.piece.shape):
                for x, cell in enumerate(row):
                    if cell:
                        px = GRID_X + (gx+x)*BLOCK_SIZE
                        py = GRID_Y + (gy+y)*BLOCK_SIZE
                        c = selected.color
                        shadow = (c[0]//2, c[1]//2, c[2]//2)
                        pygame.draw.rect(screen, shadow, (px, py, BLOCK_SIZE, BLOCK_SIZE))
                        pygame.draw.rect(screen, (255,255,255), (px, py, BLOCK_SIZE, BLOCK_SIZE), 3)

        # Preview pieces
        for i, v in enumerate(visuals[:3]):
            if v is not None and v != selected:
                v.draw(screen, preview_pos[i][0], preview_pos[i][1])

        # Dragging piece
        if selected and selected.dragging:
            selected.draw(screen, mouse[0]-selected.offset_x, mouse[1]-selected.offset_y)
        
        if game_over:
            overlay = pygame.Surface((1000, 1000), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            screen.blit(overlay, (0, 0))

            go_text = font.render("Game Over", True, (255,0,0))
            text_rect = go_text.get_rect(center=(1000 // 2, 1000 // 2))
            screen.blit(go_text, text_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

all_pieces = [G, GG, GGG, GGGG, GGGGG, GGGGGG, GGGGGGG, I, II, III, IIII, IIIII, IIIIII, IIIIIII, IIIIIIII, O, OO, OOO, OOOO, T, TT, TTT, TTTT, J, JJ, JJJ, JJJJ, L, LL, LLL, LLLL, S, SS, SSS, SSSS]

show_in_window(all_pieces, LOOT_TABLE)