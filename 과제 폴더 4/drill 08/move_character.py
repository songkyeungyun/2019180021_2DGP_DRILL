from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

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


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
dirx = 0
diry = 0
dir= 0
while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    if dir == 1:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
    elif dir == 0:
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    if x < KPU_WIDTH and y < KPU_HEIGHT and x > 0 and y > 0:
        x += dirx * 5
        if x >= KPU_WIDTH:
            x = KPU_WIDTH
            x -= dirx * 5
        elif x <= 0:
            x = 0
            x -= dirx * 5
        y += diry * 5
        if y >= KPU_HEIGHT:
            y = KPU_HEIGHT
            y -= diry * 5
        elif y <= 0:
            y = 0
            y -= diry * 5

    delay(0.01)

close_canvas()

