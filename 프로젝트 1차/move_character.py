from pico2d import *

ISAAC_WIDTH, ISAAC_HEIGHT = 900,600

def handle_events():
    global running
    global dirx, diry, dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir = 0
                dirx += 1
            elif event.key == SDLK_LEFT:
                dir = 1
                dirx -= 1
            if event.key == SDLK_UP:
                diry += 1
            elif event.key == SDLK_DOWN:
                diry -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirx -= 1
            elif event.key == SDLK_LEFT:
                dirx += 1
            if event.key == SDLK_UP:
                diry -= 1
            elif event.key == SDLK_DOWN:
                diry += 1
    pass


open_canvas(ISAAC_WIDTH, ISAAC_HEIGHT)
isaac_ground = load_image('stage0.png')
character = load_image('character_animation1.png')

running = True
x, y = ISAAC_WIDTH // 2, ISAAC_HEIGHT // 2
frame = 0
dirx = 0
diry = 0
dir= 0
while running:
    clear_canvas()
    isaac_ground.draw(ISAAC_WIDTH // 2, ISAAC_HEIGHT // 2)
    if dir == 1:
        character.clip_draw(frame * 20, 900, 30, 30, x, y)
    elif dir == 0:
        character.clip_draw(frame * 20, 900, 30, 30, x, y)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    if x < ISAAC_WIDTH and y < ISAAC_HEIGHT and x > 0 and y > 0:
        x += dirx * 5
        if x >= ISAAC_WIDTH:
            x = ISAAC_WIDTH
            x -= dirx * 5
        elif x <= 0:
            x = 0
            x -= dirx * 5
        y += diry * 5
        if y >= ISAAC_HEIGHT:
            y = ISAAC_HEIGHT
            y -= diry * 5
        elif y <= 0:
            y = 0
            y -= diry * 5

    delay(0.1)

close_canvas()

