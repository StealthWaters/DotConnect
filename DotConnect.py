from pgzrun import go
from random import randint

WIDTH = 800
HEIGHT = 450
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
    for _ in range(number_of_dots):
        actor = Actor("coin")
        actor.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
        collision = False
        for dot in dots:
            dx = actor.pos[0] - dot.pos[0]
            dy = actor.pos[1] - dot.pos[1]
            if dx * dx + dy * dy < min_distance * min_distance:
                collision = True
                break
        if not collision:
            dots.append(actor)
def draw():
    screen.fill("black")
    if game_finished:
        screen.draw.text("You beat the game!", center=(WIDTH // 2, HEIGHT // 2), fontsize=40, color="white")
        return
    
    screen.draw.text(f"Level {level}", (10,10), fontsize=30, color="white")
    
    for i, dot in enumerate(dots):
        screen.draw.text(str(i + 1), (dot.pos[0], dot.pos[1] + 12))
        dot.draw()
            
    for line in lines:
        screen.draw.line(line[0], line[1], (100,0,0))
def on_mouse_down(pos):
    global next_dot, lines, game_finished, level

    if game_finished:
        return
    
    if dots[next_dot].collidepoint(pos):
        if next_dot:
            lines.append((dots[next_dot-1].pos, dots[next_dot].pos))
        next_dot += 1
        
        if next_dot == len(dots):
            lines.append((dots[-1].pos, dots[0].pos))
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