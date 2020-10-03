# Any live cell with two or three live neighbours survives.
# Any dead cell with three live neighbours becomes a live cell.
# All other live cells die in the next generation. Similarly, all other dead cells stay dead.

#game_of_life_board_size = input("enter the board size?")

game_of_life_matrix = [
    [0, 1, 0, 1, 1],
    [0, 0, 1, 0, 1],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0]
]

for index, cell in enumerate(game_of_life_matrix):
    for index2, cell2 in enumerate(cell):
        # print(cell)
        # print(cell2)
        neighbours_array = []

        if index - 1 >= 0 and index2 - 1 >= 0:
                neighbours_array.append(game_of_life_matrix[index - 1][index2 - 1])

        if index - 1 >= 0:
            neighbours_array.append(game_of_life_matrix[index - 1][index2])

        if index - 1 >= 0 and index2 + 1 <= 2:
            neighbours_array.append(game_of_life_matrix[index - 1][index2 + 1])

        if index2 - 1 >= 0:
            neighbours_array.append(game_of_life_matrix[index][index2 - 1])

        if index2 + 1 <= 2:
            neighbours_array.append(game_of_life_matrix[index][index2 + 1])

        if index2 - 1 >= 0 and index + 1 <= 2:
            neighbours_array.append(game_of_life_matrix[index + 1][index2 - 1])
            
        if index + 1 <= 2:
            neighbours_array.append(game_of_life_matrix[index + 1][index2])

        if index + 1 <= 2 and index2 + 1 <= 2:
            neighbours_array.append(game_of_life_matrix[index + 1][index2 + 1])


        # print(index)
        # print(index2)
        # print(index2 - 1)
        # print(cell[index2 - 1])
            
        ##print(neighbours_array)

        count = 0
        for liveordead in neighbours_array:
            if liveordead == 1:
                count += 1

        if game_of_life_matrix[index][index2] == 0:
            if count == 3:
                game_of_life_matrix[index][index2] = 1
                #print("debug1")
            else:
                game_of_life_matrix[index][index2] = 0
                #print("debug2")

        if game_of_life_matrix[index][index2] == 1:
            if count == 2 or count == 3:
                game_of_life_matrix[index][index2] = 1
                #print("debug3")
            else: 
                game_of_life_matrix[index][index2] = 0
                #print("debug4")
        #print("sdfasdgvaev") 

print(game_of_life_matrix)
            
            



    #if cell == "0":
        #live_neighbour_cells = 0
        #if game_of_life_matrix[index - 1][index2 - 1] and game_of_life_matrix[index - 1][index], game_of_life_matrix[index - 1][index2 + 1] 
        #print(index, index2)
        #for game_of_life_matrix.cell[]


