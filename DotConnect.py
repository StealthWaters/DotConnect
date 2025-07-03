import os
os.environ["SDL_VIDEO_CENTERED"] = "1"  # Center the window on the screen
from pgzrun import go
from random import randint


WIDTH = 1536
HEIGHT = 800
dots = []
lines = []
next_dot = 0
game_finished = False
level = 1
base_dots = 10
max_level = 5

def setup_level():
    global dots, lines, next_dot, number_of_dots
    lines = []
    next_dot = 0
    number_of_dots = base_dots + (level - 1) * 5
    dots = []
    min_distance = 60
    while len(dots) < number_of_dots:
        pos = randint(40, WIDTH - 40), randint(40, HEIGHT - 40)
        collision = False
        for dot in dots:
            dx = pos[0] - dot[0]
            dy = pos[1] - dot[1]
            if dx * dx + dy * dy < min_distance * min_distance:
                collision = True
                break
        if not collision:
            dots.append(pos)
def draw():
    screen.fill("white") # type: ignore
    if game_finished:
        screen.draw.text("You beat the game!", center=(WIDTH // 2, HEIGHT // 2), fontsize=40, color="black") # type: ignore
        screen.draw.text("Restart to play again.", center=(WIDTH // 2, HEIGHT // 2 + 40), fontsize=30, color="black") # type: ignore
        return

    screen.draw.text(f"Level {level}", (10,10), fontsize=30, color="black") # type: ignore

    for i, dot in enumerate(dots):
        screen.draw.text(str(i + 1), (dot[0], dot[1] + 12), fontsize=20, color="black") # type: ignore
        screen.draw.circle(dot, 8, "black") # type: ignore

    for line in lines:
        screen.draw.line(line[0], line[1], "black") # type: ignore
def on_mouse_down(pos):
    global next_dot, lines, game_finished, level

    if game_finished:
        return

    dot_pos = dots[next_dot]
    dx = pos[0] - dot_pos[0]
    dy = pos[1] - dot_pos[1]
    if dx * dx + dy * dy < 15 * 15:  # 15 is the dot "radius"
        if next_dot:
            lines.append((dots[next_dot-1], dots[next_dot]))
        next_dot += 1

        if next_dot == len(dots):
            lines.append((dots[-1], dots[0]))
            if level < max_level:
                level += 1
                setup_level()
            else:
                game_finished = True
    else:
        level = 1
        setup_level()
setup_level()
go()
