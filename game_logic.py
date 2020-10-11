# Any live cell with two or three live neighbours survives.
# Any dead cell with three live neighbours becomes a live cell.
# All other live cells die in the next generation. Similarly, all other dead cells stay dead.

#game_of_life_board_size = input("enter the board size?")
import copy
import random
game_of_life_matrix = []

#world_size_x = int(input("enter x"))
#world_size_y = int(input("enter y"))

#def get_next_turn_world():
    #global game_of_life_matrix
    #return game_of_life_matrix

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
    game_of_life_matrix[1][3] = 1
    game_of_life_matrix[2][4] = 1
    game_of_life_matrix[3][2] = 1
    game_of_life_matrix[3][3] = 1
    game_of_life_matrix[3][4] = 1

def randomize_alive_cells(percent_of_cells = 50):
    global game_of_life_matrix
    world_size_x, world_size_y = get_world_size()
    world_cells_count = world_size_x * world_size_y
    alive_cells_required = int((percent_of_cells/100)*world_cells_count)
    for i in range(alive_cells_required):
        cell_x = random.randint(0, world_size_x-1)
        cell_y = random.randint(0, world_size_y-1)
        while game_of_life_matrix[cell_x][cell_y] == 1:
            cell_x = random.randint(0, world_size_x-1)
            cell_y = random.randint(0, world_size_y-1)
        game_of_life_matrix[cell_x][cell_y] = 1

def get_next_turn_world():
    global game_of_life_matrix
    temp_matrix = copy.deepcopy(game_of_life_matrix)
    for index, cell in enumerate(game_of_life_matrix):
        for index2, cell2 in enumerate(cell):
            neighbours_array = []

            if index - 1 >= 0 and index2 - 1 >= 0:
                neighbours_array.append(game_of_life_matrix[index - 1][index2 - 1])

            if index - 1 >= 0:
                neighbours_array.append(game_of_life_matrix[index - 1][index2])

            if index - 1 >= 0 and index2 + 1 <= len(cell)-1:
                neighbours_array.append(game_of_life_matrix[index - 1][index2 + 1])

            if index2 - 1 >= 0:
                neighbours_array.append(game_of_life_matrix[index][index2 - 1])

            if index2 + 1 <= len(cell)-1:
                neighbours_array.append(game_of_life_matrix[index][index2 + 1])

            if index2 - 1 >= 0 and index + 1 <= len(game_of_life_matrix)-1:
                neighbours_array.append(game_of_life_matrix[index + 1][index2 - 1])

            if index + 1 <= len(game_of_life_matrix)-1:
                neighbours_array.append(game_of_life_matrix[index + 1][index2])

            if index + 1 <= len(game_of_life_matrix)-1 and index2 + 1 <= len(cell)-1:
                neighbours_array.append(game_of_life_matrix[index + 1][index2 + 1])

            count = 0
            for liveordead in neighbours_array:
                if liveordead == 1:
                    count += 1

            if game_of_life_matrix[index][index2] == 0:
                if count == 3:
                    temp_matrix[index][index2] = 1
                else:
                    temp_matrix[index][index2] = 0

            if game_of_life_matrix[index][index2] == 1:
                if count == 2 or count == 3:
                    temp_matrix[index][index2] = 1
                else:
                    temp_matrix[index][index2] = 0

    game_of_life_matrix = copy.deepcopy(temp_matrix)
    return game_of_life_matrix

# init_world(world_size_x, world_size_y)
# #get_game_world()
# print(game_of_life_matrix)
# #print(game_of_life_matrix_new_cell_state)
