"""
Pygame Snake - single-file

Controls:
  Arrow keys or WASD - move
  P                 - pause/unpause
  R                 - restart after game over
  Esc               - quit

How to run:
  pip install pygame
  python snake_game.py

Classic snake: eat food to grow, avoid hitting yourself or (optionally) walls.
"""

import pygame
import random
import sys
from dataclasses import dataclass

# ------------------ Config ------------------
CELL_SIZE = 20
COLS = 40  # 40 * 20 = 800
ROWS = 30  # 30 * 20 = 600
WIDTH, HEIGHT = CELL_SIZE * COLS, CELL_SIZE * ROWS
FPS = 60
MOVE_EVENT = pygame.USEREVENT + 1
MOVE_DELAY = 120  # milliseconds between snake moves (will speed up)

WRAP_AROUND = False  # If True, snake wraps at edges. If False, hitting wall = game over.

# Colors
BG = (18, 18, 20)
GRID = (30, 30, 36)
SNAKE_HEAD = (94, 164, 90)
SNAKE_BODY = (72, 140, 72)
FOOD = (240, 120, 40)
TEXT = (220, 220, 220)
RED = (200, 60, 60)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

FONT_LG = pygame.font.SysFont("arialroundedmtbold", 48)
FONT_MD = pygame.font.SysFont("arialroundedmtbold", 28)
FONT_SM = pygame.font.SysFont("arial", 18)


@dataclass
class GameState:
    snake: list  # list of (x, y) cells
    direction: tuple
    next_direction: tuple
    food: tuple
    score: int
    speed: int  # move delay in ms
    running: bool
    paused: bool
    game_over: bool


def random_food(snake):
    while True:
        x = random.randrange(0, COLS)
        y = random.randrange(0, ROWS)
        if (x, y) not in snake:
            return (x, y)


def init_state():
    mid = (COLS // 2, ROWS // 2)
    snake = [mid, (mid[0] - 1, mid[1]), (mid[0] - 2, mid[1])]
    direction = (1, 0)  # moving right
    food = random_food(snake)
    return GameState(snake=snake,
                     direction=direction,
                     next_direction=direction,
                     food=food,
                     score=0,
                     speed=MOVE_DELAY,
                     running=True,
                     paused=False,
                     game_over=False)


def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRID, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRID, (0, y), (WIDTH, y))


def draw_state(state: GameState):
    screen.fill(BG)
    draw_grid()

    # Draw food
    fx, fy = state.food
    pygame.draw.rect(screen, FOOD, (fx * CELL_SIZE + 2, fy * CELL_SIZE + 2, CELL_SIZE - 4, CELL_SIZE - 4), border_radius=6)

    # Draw snake
    for i, (sx, sy) in enumerate(state.snake):
        rect = pygame.Rect(sx * CELL_SIZE + 1, sy * CELL_SIZE + 1, CELL_SIZE - 2, CELL_SIZE - 2)
        color = SNAKE_HEAD if i == 0 else SNAKE_BODY
        pygame.draw.rect(screen, color, rect, border_radius=6)

    # HUD
    score_surf = FONT_MD.render(f"Score: {state.score}", True, TEXT)
    screen.blit(score_surf, (8, 8))
    speed_surf = FONT_SM.render(f"Speed: {int(1000/state.speed) if state.speed>0 else 0} moves/sec", True, TEXT)
    screen.blit(speed_surf, (8, 40))

    if state.paused:
        label = FONT_LG.render("Paused", True, TEXT)
        screen.blit(label, (WIDTH // 2 - label.get_width() // 2, HEIGHT // 2 - label.get_height() // 2))

    if state.game_over:
        over = FONT_LG.render("Game Over", True, RED)
        sub = FONT_MD.render(f"Score: {state.score}   Press R to restart", True, TEXT)
        screen.blit(over, (WIDTH // 2 - over.get_width() // 2, HEIGHT // 2 - 60))
        screen.blit(sub, (WIDTH // 2 - sub.get_width() // 2, HEIGHT // 2 + 6))


def step(state: GameState):
    # Apply next_direction if it's not directly opposite
    ndx, ndy = state.next_direction
    dx, dy = state.direction
    if (ndx, ndy) != (-dx, -dy):
        state.direction = (ndx, ndy)

    head = state.snake[0]
    new_head = (head[0] + state.direction[0], head[1] + state.direction[1])

    # Handle wrap or wall collisions
    if WRAP_AROUND:
        new_head = (new_head[0] % COLS, new_head[1] % ROWS)
    else:
        if not (0 <= new_head[0] < COLS and 0 <= new_head[1] < ROWS):
            state.game_over = True
            return

    # Check self-collision
    if new_head in state.snake:
        state.game_over = True
        return

    # Move snake
    state.snake.insert(0, new_head)

    # Eat food?
    if new_head == state.food:
        state.score += 1
        # speed up slightly every few points
        if state.score % 3 == 0 and state.speed > 40:
            state.speed = max(40, state.speed - 8)
            pygame.time.set_timer(MOVE_EVENT, state.speed)
        state.food = random_food(state.snake)
    else:
        state.snake.pop()


def handle_key(event_key, state: GameState):
    if event_key in (pygame.K_LEFT, pygame.K_a):
        state.next_direction = (-1, 0)
    elif event_key in (pygame.K_RIGHT, pygame.K_d):
        state.next_direction = (1, 0)
    elif event_key in (pygame.K_UP, pygame.K_w):
        state.next_direction = (0, -1)
    elif event_key in (pygame.K_DOWN, pygame.K_s):
        state.next_direction = (0, 1)
    elif event_key == pygame.K_p:
        state.paused = not state.paused
    elif event_key == pygame.K_r and state.game_over:
        return init_state()
    elif event_key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()
    return state


def main():
    state = init_state()
    pygame.time.set_timer(MOVE_EVENT, state.speed)

    while state.running:
        dt = clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state.running = False
            elif event.type == pygame.KEYDOWN:
                # direct key handling
                state = handle_key(event.key, state)
            elif event.type == MOVE_EVENT:
                if not state.paused and not state.game_over:
                    step(state)

        draw_state(state)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
