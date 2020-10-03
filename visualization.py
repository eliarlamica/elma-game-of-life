import random
import time

from bokeh.plotting import figure, curdoc
from bokeh.models import Button
from bokeh.layouts import column

import game_logic

_rectangles_data_source = []
_rectangles_data_dead_source = []
_size_of_cell = 20
_callback_id = 0

def get_game_world():
    return game_logic.get_game_world()
    # return [[random.randint(0,1),random.randint(0,1),random.randint(0,1)],[random.randint(0,1),random.randint(0,1),random.randint(0,1)],[random.randint(0,1),random.randint(0,1),random.randint(0,1)],[random.randint(0,1),random.randint(0,1),random.randint(0,1)],[random.randint(0,1),random.randint(0,1),random.randint(0,1)]]

def draw():
    live_cells_x = []
    live_cells_y = []
    dead_cells_x = []
    dead_cells_y = []

    game_world = get_game_world()
    print(game_world)

    global _size_of_cell
    for x, row in enumerate(game_world):
        for y, cell in enumerate(row):
            if cell == 1:
                live_cells_x.append(x*_size_of_cell)
                live_cells_y.append(y*_size_of_cell)
            if cell == 0:
                dead_cells_x.append(x*_size_of_cell)
                dead_cells_y.append(y*_size_of_cell)

    global _rectangles_data_source
    _rectangles_data_source.data['y'] = live_cells_x
    _rectangles_data_source.data['x'] = live_cells_y
    global _rectangles_data_dead_source
    _rectangles_data_dead_source.data['y'] = dead_cells_x
    _rectangles_data_dead_source.data['x'] = dead_cells_y

def start_auto_turn():
    global _callback_id
    _callback_id = curdoc().add_periodic_callback(draw, 500)

def stop_auto_turn():
    global _callback_id
    curdoc().remove_periodic_callback(_callback_id)

def init_canvas(canvas_width = 400, canvas_height = 400):
    p = figure(plot_width=canvas_width, plot_height=canvas_height)
    global _size_of_cell
    rectangles = p.rect([], [], width=_size_of_cell, height=_size_of_cell, color="red", alpha=0.5)
    global _rectangles_data_source
    _rectangles_data_source = rectangles.data_source

    rectangles_dead = p.rect([], [], width=_size_of_cell, height=_size_of_cell, color="black", alpha=0.2)
    global _rectangles_data_dead_source
    _rectangles_data_dead_source = rectangles_dead.data_source

    next_turn_button = Button(label="Next Turn")
    next_turn_button.on_click(draw)

    start_auto_button = Button(label="Start Auto")
    start_auto_button.on_click(start_auto_turn)

    stop_auto_button = Button(label="Stop Auto")
    stop_auto_button.on_click(stop_auto_turn)

    curdoc().add_root(column(next_turn_button, start_auto_button, stop_auto_button, p))

init_canvas()
