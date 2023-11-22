import random
import json
import os

from pico2d import *
import game_framework
import game_world

import server
from boy import Boy
from ball import Ball

# fill here
from background import FixedBackground as Background





def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            server.boy.handle_event(event)



def init():
    # fill here
    server.background = Background()
    server.boy = Boy()

    balls = [ Ball() for _ in range(100)]

    game_world.add_objects(balls,1)
    game_world.add_object(server.background,0)
    game_world.add_object(server.boy,1)

    game_world.add_collision_pair("Boy : Ball",server.boy,None)

    for ball in balls:
        game_world.add_collision_pair("Boy : Ball",None,ball)
        ball.set_background(server.background)



    # notice to boy for his Background
    server.boy.set_background(server.background)


def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    game_world.handle_collisions()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass



