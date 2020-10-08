# Any live cell with two or three live neighbours survives.
# Any dead cell with three live neighbours becomes a live cell.
# All other live cells die in the next generation. Similarly, all other dead cells stay dead.

#game_of_life_board_size = input("enter the board size?")
import copy
game_of_life_matrix = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0],
]

game_of_life_matrix_new_cell_state = copy.deepcopy(game_of_life_matrix)

def get_game_world():
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
                    game_of_life_matrix_new_cell_state[index][index2] = 1
                    print("thisisif1")
                else:
                    game_of_life_matrix_new_cell_state[index][index2] = 0

            if game_of_life_matrix[index][index2] == 1:
                if count == 2 or count == 3:
                    game_of_life_matrix_new_cell_state[index][index2] = 1
                else:
                    game_of_life_matrix_new_cell_state[index][index2] = 0

    return game_of_life_matrix

get_game_world()
print(game_of_life_matrix)
print(game_of_life_matrix_new_cell_state)
