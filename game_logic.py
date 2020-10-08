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
    # print(world_size_x, "вот оно!")
    # print(world_size_y, "вот оно!")
    
    #percent = 90
    #nums = percent * [1] + (100 - percent) * [0]
    game_of_life_matrix = [[random.randint(0, 1) for x in range(world_size_x)] for y in range(world_size_y)]
    

#game_of_life_matrix_new_cell_state = copy.deepcopy(game_of_life_matrix)

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

            if index2 - 1 >= 0 and index + 1 <= len(cell)-1:
                neighbours_array.append(game_of_life_matrix[index + 1][index2 - 1])

            if index + 1 <= len(cell)-1:
                neighbours_array.append(game_of_life_matrix[index + 1][index2])

            if index + 1 <= len(cell)-1 and index2 + 1 <= len(cell)-1:
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
