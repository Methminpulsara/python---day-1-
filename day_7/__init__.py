import pygame
import random
import sys
from dataclasses import dataclass

# ---------------------------------------------
# Coin Catch – a tiny Pygame arcade game
# ---------------------------------------------
# Controls
#   ←/→  or  A/D : Move
#   P            : Pause/Unpause
#   R            : Restart (from Game Over)
#   Esc          : Quit
# ---------------------------------------------

# --- Config ---
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (40, 40, 48)
LIGHT_GRAY = (200, 200, 210)
GOLD = (252, 201, 0)
SILVER = (192, 192, 192)
GREEN = (80, 220, 120)
RED = (230, 80, 80)
CYAN = (60, 200, 220)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Catch")
clock = pygame.time.Clock()

# Fonts
FONT_LG = pygame.font.SysFont("arialroundedmtbold", 48)
FONT_MD = pygame.font.SysFont("arialroundedmtbold", 28)
FONT_SM = pygame.font.SysFont("arial", 20)


@dataclass
class Player:
    w: int = 110
    h: int = 24
    speed: float = 8

    def __post_init__(self):
        self.rect = pygame.Rect((WIDTH - self.w) // 2, HEIGHT - 80, self.w, self.h)
        self.vx = 0

    def update(self, pressed):
        self.vx = 0
        if pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
            self.vx = -self.speed
        if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
            self.vx = self.speed
        self.rect.x += int(self.vx)
        self.rect.x = max(0, min(WIDTH - self.rect.width, self.rect.x))

    def draw(self, surf):
        # Smooth rounded catcher with a subtle highlight
        pygame.draw.rect(surf, CYAN, self.rect, border_radius=10)
        lip = self.rect.inflate(-8, -8)
        lip.height = max(8, lip.height // 3)
        lip.y = self.rect.y + 4
        pygame.draw.rect(surf, WHITE, lip, width=2, border_radius=8)


class Coin:
    def __init__(self, x, y, r, speed, kind="gold"):
        self.x = x
        self.y = y
        self.r = r
        self.speed = speed
        self.kind = kind  # "gold" or "silver" or "bomb"
        # Give each coin a slight horizontal drift
        self.vx = random.uniform(-0.5, 0.5)

    def update(self):
        self.y += self.speed
        self.x += self.vx

    @property
    def rect(self):
        return pygame.Rect(int(self.x - self.r), int(self.y - self.r), self.r * 2, self.r * 2)

    def draw(self, surf):
        if self.kind == "bomb":
            pygame.draw.circle(surf, RED, (int(self.x), int(self.y)), self.r)
            # fuse
            pygame.draw.line(surf, BLACK, (int(self.x), int(self.y - self.r)), (int(self.x + self.r * 0.7), int(self.y - self.r * 1.5)), 3)
        else:
            color = GOLD if self.kind == "gold" else SILVER
            pygame.draw.circle(surf, color, (int(self.x), int(self.y)), self.r)
            pygame.draw.circle(surf, WHITE, (int(self.x), int(self.y)), self.r, 2)


class Starfield:
    def __init__(self, n=80):
        self.stars = [(random.randrange(0, WIDTH), random.randrange(0, HEIGHT), random.randint(1, 3)) for _ in range(n)]

    def update(self):
        for i, (x, y, s) in enumerate(self.stars):
            y += s
            if y > HEIGHT:
                y = 0
                x = random.randrange(0, WIDTH)
                s = random.randint(1, 3)
            self.stars[i] = (x, y, s)

    def draw(self, surf):
        for x, y, s in self.stars:
            pygame.draw.circle(surf, (90 + s * 20, 90 + s * 20, 110 + s * 20), (x, y), s)


class Game:
    def __init__(self):
        self.player = Player()
        self.starfield = Starfield()
        self.reset()
        self.state = "menu"  # menu, playing, paused, over
        self.high_score = 0

    def reset(self):
        self.score = 0
        self.lives = 3
        self.level = 1
        self.coins = []
        self.spawn_timer = 0
        self.spawn_interval = 650  # ms
        self.drop_speed = 3.2

    def spawn_coin(self):
        r = random.randint(10, 16)
        x = random.randint(r, WIDTH - r)
        y = -r
        # choose kind with small chance of silver (worth 3) & bomb (avoid)
        roll = random.random()
        if roll < 0.12:
            kind = "silver"
        elif roll < 0.22:
            kind = "bomb"
        else:
            kind = "gold"
        speed = self.drop_speed + random.uniform(-0.4, 0.6)
        self.coins.append(Coin(x, y, r, speed, kind))

    def update_difficulty(self):
        # Increase difficulty as score climbs
        self.level = 1 + self.score // 20
        self.drop_speed = 3.2 + (self.level - 1) * 0.45
        self.spawn_interval = max(260, 650 - (self.level - 1) * 35)
        self.player.speed = 7 + min(4, self.level // 2)

    def circle_rect_collide(self, circle: Coin, rect: pygame.Rect):
        # Clamp point to rect
        cx, cy, r = circle.x, circle.y, circle.r
        rx = max(rect.left, min(cx, rect.right))
        ry = max(rect.top, min(cy, rect.bottom))
        dx = cx - rx
        dy = cy - ry
        return dx*dx + dy*dy <= r*r

    def handle_catches_and_misses(self):
        # Catch coins
        caught_any = False
        for coin in self.coins[:]:
            if self.circle_rect_collide(coin, self.player.rect):
                if coin.kind == "bomb":
                    self.lives -= 1
                else:
                    gained = 3 if coin.kind == "silver" else 1
                    self.score += gained
                self.coins.remove(coin)
                caught_any = True
        # Remove coins that fell off screen
        for coin in self.coins[:]:
            if coin.y - coin.r > HEIGHT:
                if coin.kind != "bomb":
                    self.lives -= 1
                self.coins.remove(coin)
        return caught_any

    def draw_hud(self, surf):
        bar = pygame.Rect(0, 0, WIDTH, 56)
        pygame.draw.rect(surf, (20, 20, 26), bar)
        pygame.draw.line(surf, (60, 60, 72), (0, bar.bottom), (WIDTH, bar.bottom), 2)

        score_s = FONT_MD.render(f"Score: {self.score}", True, WHITE)
        lives_s = FONT_MD.render("❤ " * self.lives + "  " * max(0, 3 - self.lives), True, RED)
        level_s = FONT_MD.render(f"Lv {self.level}", True, LIGHT_GRAY)
        hs_s = FONT_SM.render(f"High: {self.high_score}", True, LIGHT_GRAY)
        surf.blit(score_s, (16, 14))
        surf.blit(level_s, (WIDTH // 2 - level_s.get_width() // 2, 14))
        surf.blit(lives_s, (WIDTH - lives_s.get_width() - 16, 10))
        surf.blit(hs_s, (WIDTH - hs_s.get_width() - 16, 34))

    def draw_centered_text(self, lines, color=WHITE, subcolor=LIGHT_GRAY):
        # Draw title + sublines centered
        y = HEIGHT // 2 - len(lines) * 22
        for i, (text, big) in enumerate(lines):
            font = FONT_LG if big else FONT_MD
            s = font.render(text, True, color if big else subcolor)
            x = WIDTH // 2 - s.get_width() // 2
            screen.blit(s, (x, y))
            y += s.get_height() + (8 if big else 4)

    def run(self):
        running = True
        last_spawn = pygame.time.get_ticks()
        while running:
            dt = clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if self.state == "menu" and event.key in (pygame.K_SPACE, pygame.K_RETURN):
                        self.reset()
                        self.state = "playing"
                    elif self.state == "playing" and event.key == pygame.K_p:
                        self.state = "paused"
                    elif self.state == "paused" and event.key == pygame.K_p:
                        self.state = "playing"
                    elif self.state == "over" and event.key == pygame.K_r:
                        self.reset()
                        self.state = "playing"

            screen.fill(GRAY)
            self.starfield.update()
            self.starfield.draw(screen)

            if self.state == "menu":
                title_lines = [
                    ("COIN CATCH", True),
                    ("Move with ← →  (A/D)", False),
                    ("Catch gold & silver coins. Avoid bombs.", False),
                    ("Press SPACE to start", False),
                ]
                self.draw_centered_text(title_lines)

            elif self.state == "paused":
                self.draw_gameplay(dt)
                self.draw_centered_text([("Paused", True), ("Press P to resume", False)])

            elif self.state == "over":
                self.draw_gameplay(dt, advance=False)
                self.high_score = max(self.high_score, self.score)
                over_lines = [
                    ("Game Over", True),
                    (f"Score: {self.score}  |  High: {self.high_score}", False),
                    ("Press R to play again", False),
                ]
                self.draw_centered_text(over_lines)

            elif self.state == "playing":
                self.update_difficulty()
                self.update_gameplay(dt)
                self.draw_gameplay(dt)
                if self.lives <= 0:
                    self.state = "over"

            pygame.display.flip()
        pygame.quit()
        sys.exit()

    def update_gameplay(self, dt):
        pressed = pygame.key.get_pressed()
        self.player.update(pressed)

        now = pygame.time.get_ticks()
        if now - self.spawn_timer > self.spawn_interval:
            self.spawn_timer = now
            # spawn 1-2 coins occasionally
            for _ in range(1 + (1 if random.random() < 0.18 else 0)):
                self.spawn_coin()

        for c in self.coins:
            c.update()
        self.handle_catches_and_misses()

    def draw_gameplay(self, dt, advance=True):
        # Draw coins
        for c in self.coins:
            c.draw(screen)
        # Draw player & HUD
        self.player.draw(screen)
        self.draw_hud(screen)


if __name__ == "__main__":
    Game().run()
