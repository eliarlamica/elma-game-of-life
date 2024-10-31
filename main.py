from game_logic import init_world, randomize_alive_cells
from visualization import init_canvas


def main():
    print("Starting Elma Game of Life..")

    world_size_x = int(input("Please provide X size of world\n"))
    world_size_y = int(input("Please provide Y size of world\n"))
    init_world(world_size_x, world_size_y)
    randomize_alive_cells()
    init_canvas()

    print("Elma Game of Life finished!")


if __name__ == "__main__":
    print("Error, main.py must be launched via bokeh, not directly!")
    print("bokeh serve --show main.py")
else:
    main()
