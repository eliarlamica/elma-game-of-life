
import argparse

import game_logic
import visualization

print("Starting Game Of Life..")

world_size_x = 100
world_size_y = 50
game_logic.init_world(world_size_x, world_size_y)
game_logic.randomize_alive_cells()
visualization.init_canvas()

print("Game Of Life work finished. Thank You for Your time!")