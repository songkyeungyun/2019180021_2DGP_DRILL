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
character = load_image('oo.png')
monster1 = load_image('monster1 animation.png')
monster2 = load_image('monster2 animation.png')

running = True
x, y = ISAAC_WIDTH // 2, ISAAC_HEIGHT // 2
frame1 = 0
frame2 = 0
frame3 = 0
dirx = 0
diry = 0
dir= 0
stage=0
while running:
    if stage == 0:
        clear_canvas()
        isaac_ground.draw(ISAAC_WIDTH // 2, ISAAC_HEIGHT // 2)
        if dir == 1:
            character.clip_draw(frame1 * 66, 100, 60, 120, x, y)
        elif dir == 0:
            character.clip_draw(frame1 * 66, 0, 60, 100, x, y)
        monster1.clip_draw(frame2 * 30, 30, 25, 60, x - 100, y)
        monster2.clip_draw(frame3 * 33, 30, 25, 35, x + 100, y)
        update_canvas()
        handle_events()
        frame1 = (frame1 + 1) % 8
        frame2 = (frame2 + 1) % 6
        frame3 = (frame3 + 1) % 4
        if x < 770 and y < 420 and x > 130 and y > 80:
            x += dirx * 5
            if x >= 770:
                x -= dirx * 5
            elif x <= 130:
                if x>= 130 and y <= 255 and y> 240:
                    isaac_ground = load_image('stage5.png')
                    x = 760
                    stage = 5
                x -= dirx * 5
            y += diry * 5
            if y >= 420:
                if y<=420 and x >= 445 and x<= 455:
                    isaac_ground = load_image('stage1.png')
                    y = 90
                    stage = 1
                y -= diry * 5
            elif y <= 80:
                if y>=80 and x>=445 and x<=455:
                    isaac_ground = load_image('stage2.png')
                    y = 410
                    stage = 2
                y -= diry * 5
    elif stage == 1:
        clear_canvas()
        isaac_ground.draw(ISAAC_WIDTH // 2, ISAAC_HEIGHT // 2)
        if dir == 1:
            character.clip_draw(frame * 66  , 100, 60, 120, x, y)
        elif dir == 0:
            character.clip_draw(frame * 66  , 0, 60, 100, x, y)
        update_canvas()

        handle_events()
        frame = (frame + 1) % 8
        if x < 770 and y < 420 and x > 130 and y > 80:
            x += dirx * 5
            if x >= 770:
                x -= dirx * 5
            elif x <= 130:
                x -= dirx * 5
            y += diry * 5
            if y >= 420:
                y -= diry * 5
            elif y <= 80:
                if y>=80 and x>=445 and x<=455:
                    isaac_ground = load_image('stage0.png')
                    y = 410
                    stage = 0
                y -= diry * 5
    elif stage == 5:
        clear_canvas()
        isaac_ground.draw(ISAAC_WIDTH // 2, ISAAC_HEIGHT // 2)
        if dir == 1:
            character.clip_draw(frame * 66  , 100, 60, 120, x, y)
        elif dir == 0:
            character.clip_draw(frame * 66  , 0, 60, 100, x, y)
        update_canvas()

        handle_events()
        frame = (frame + 1) % 8
        if x < 770 and y < 420 and x > 130 and y > 80:
            x += dirx * 5
            if x >= 770:
                if x <= 770 and y>= 240 and y<= 255:
                    isaac_ground = load_image('stage0.png')
                    stage = 0
                    x = 140
                x -= dirx * 5
            elif x <= 130:
                x -= dirx * 5
            y += diry * 5
            if y >= 420:
                y -= diry * 5
            elif y <= 80:
                y -= diry * 5
    elif stage == 2:
        clear_canvas()
        isaac_ground.draw(ISAAC_WIDTH // 2, ISAAC_HEIGHT // 2)
        if dir == 1:
            character.clip_draw(frame * 66  , 100, 60, 120, x, y)
        elif dir == 0:
            character.clip_draw(frame * 66  , 0, 60, 100, x, y)
        update_canvas()
        
        handle_events()
        frame = (frame + 1) % 8
        if x < 770 and y < 420 and x > 130 and y > 80:
            x += dirx * 5
            if x >= 770:
                x -= dirx * 5
            elif x <= 130:
                x -= dirx * 5
            y += diry * 5
            if y >= 420:
                if y <= 420 and x >= 445 and x <= 455:
                    isaac_ground = load_image('stage0.png')
                    y = 90
                    stage = 0
                y -= diry * 5
            elif y <= 80:
                y -= diry * 5
    delay(0.03)

close_canvas()

