from bokeh.plotting import figure, curdoc
from bokeh.models import Button
from bokeh.layouts import column

import game_logic

_callback_id = 0


class WorldCanvas:
    def __init__(self, canvas_width, canvas_height, cell_size, live_cell_visualization):
        if len(live_cell_visualization) == 2:
            self.live_cell_color = live_cell_visualization[0]
            self.live_cell_alpha = live_cell_visualization[1]
        self.cell_size = cell_size
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

        self.canvas = figure(
            width=self.canvas_width, height=self.canvas_height
        )
        self.add_buttons()
        self.add_cells()

    def add_buttons(self):
        next_turn_button = Button(label="Next Turn")
        next_turn_button.on_click(next_turn)

        start_auto_button = Button(label="Start Auto")
        start_auto_button.on_click(start_auto_turn)

        stop_auto_button = Button(label="Stop Auto")
        stop_auto_button.on_click(stop_auto_turn)

        curdoc().add_root(
            column(next_turn_button, start_auto_button, stop_auto_button, self.canvas)
        )

    def add_cells(self):
        rectangles = self.canvas.rect(
            [],
            [],
            width=self.cell_size,
            height=self.cell_size,
            line_width=0.1,
            line_color="gray",
            color=self.live_cell_color,
            alpha=self.live_cell_alpha,
        )
        self.alive_cells_data = rectangles.data_source

        rectangles_dead = self.canvas.rect(
            [],
            [],
            width=self.cell_size,
            height=self.cell_size,
            line_width=0.1,
            line_color="gray",
            color="white",
            alpha=1.0,
        )
        self.dead_cells_data = rectangles_dead.data_source


def get_next_turn_world():
    return game_logic.get_next_turn_world()


def next_turn():
    live_cells_x = []
    live_cells_y = []
    dead_cells_x = []
    dead_cells_y = []

    game_world = get_next_turn_world()

    global _world_canvas
    for x, row in enumerate(game_world):
        for y, cell in enumerate(row):
            if cell == 1:
                live_cells_x.append(x * _world_canvas.cell_size)
                live_cells_y.append(y * _world_canvas.cell_size)
            if cell == 0:
                dead_cells_x.append(x * _world_canvas.cell_size)
                dead_cells_y.append(y * _world_canvas.cell_size)

    dead_cells_data = {"x": dead_cells_x, "y": dead_cells_y}
    _world_canvas.dead_cells_data.data = dead_cells_data
    live_cells_data = {"x": live_cells_x, "y": live_cells_y}
    _world_canvas.alive_cells_data.data = live_cells_data


def start_auto_turn():
    global _callback_id
    _callback_id = curdoc().add_periodic_callback(next_turn, 500)


def stop_auto_turn():
    global _callback_id
    curdoc().remove_periodic_callback(_callback_id)


def init_canvas(canvas_width=400, canvas_height=400, size_of_cell=20):
    global _world_canvas
    _world_canvas = WorldCanvas(
        canvas_width, canvas_height, size_of_cell, ("yellow", 0.5)
    )
