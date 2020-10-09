import game_logic
import visualization

print("Starting Game Of Life..")

world_size_x = int(input("Please provide X size of world\n"))
world_size_y = int(input("Please provide Y size of world\n"))
game_logic.init_world(world_size_x, world_size_y)
game_logic.randomize_alive_cells()
visualization.init_canvas()
