import copy
import random
game_of_life_matrix = []

def init_world(world_size_x, world_size_y):
    global game_of_life_matrix
    game_of_life_matrix = [[0 for x in range(world_size_x)] for y in range(world_size_y)]

def get_world():
    global game_of_life_matrix
    return game_of_life_matrix

def get_world_size():
    global game_of_life_matrix
    world_size_x = len(game_of_life_matrix)
    if game_of_life_matrix:
        world_size_y = len(game_of_life_matrix[0])
    return (world_size_x, world_size_y)

def place_glider():
    global game_of_life_matrix
    game_of_life_matrix[1][3] = 1; 
    game_of_life_matrix[2][4] = 1;
    game_of_life_matrix[3][2] = 1;
    game_of_life_matrix[3][3] = 1;
    game_of_life_matrix[3][4] = 1;

def randomize_alive_cells(percent_of_cells = 50):
    global game_of_life_matrix
    world_size_x, world_size_y = get_world_size()
    world_cells_count = world_size_x * world_size_y
    alive_cells_required = int((percent_of_cells/100)*world_cells_count);
    for i in range(alive_cells_required):
        cell_x = random.randint(0, world_size_x-1)
        cell_y = random.randint(0, world_size_y-1)
        while game_of_life_matrix[cell_x][cell_y] == 1:
            cell_x = random.randint(0, world_size_x-1)
            cell_y = random.randint(0, world_size_y-1)
        game_of_life_matrix[cell_x][cell_y] = 1;

def get_next_turn_world():
    global game_of_life_matrix
    temp_matrix = copy.deepcopy(game_of_life_matrix)
    for row_number, row_in_matrix in enumerate(game_of_life_matrix):
        for cell_number, cell_state in enumerate(row_in_matrix):
            neighbours_array = []

            if row_number - 1 >= 0 and cell_number - 1 >= 0:
                neighbours_array.append(game_of_life_matrix[row_number - 1][cell_number - 1])

            if row_number - 1 >= 0:
                neighbours_array.append(game_of_life_matrix[row_number - 1][cell_number])

            if row_number - 1 >= 0 and cell_number + 1 <= len(row_in_matrix)-1:
                neighbours_array.append(game_of_life_matrix[row_number - 1][cell_number + 1])

            if cell_number - 1 >= 0:
                neighbours_array.append(game_of_life_matrix[row_number][cell_number - 1])

            if cell_number + 1 <= len(row_in_matrix)-1:
                neighbours_array.append(game_of_life_matrix[row_number][cell_number + 1])

            if cell_number - 1 >= 0 and row_number + 1 <= len(game_of_life_matrix)-1:
                neighbours_array.append(game_of_life_matrix[row_number + 1][cell_number - 1])

            if row_number + 1 <= len(game_of_life_matrix)-1:
                neighbours_array.append(game_of_life_matrix[row_number + 1][cell_number])

            if row_number + 1 <= len(game_of_life_matrix)-1 and cell_number + 1 <= len(row_in_matrix)-1:
                neighbours_array.append(game_of_life_matrix[row_number + 1][cell_number + 1])

            alive_cells_count = 0
            for liveordead in neighbours_array:
                if liveordead == 1:
                    alive_cells_count += 1

            if cell_state == 0:
                if alive_cells_count == 3:
                    temp_matrix[row_number][cell_number] = 1
                else:
                    temp_matrix[row_number][cell_number] = 0

            if cell_state == 1:
                if alive_cells_count == 2 or alive_cells_count == 3:
                    temp_matrix[row_number][cell_number] = 1
                else:
                    temp_matrix[row_number][cell_number] = 0

    game_of_life_matrix = copy.deepcopy(temp_matrix)
    return game_of_life_matrix