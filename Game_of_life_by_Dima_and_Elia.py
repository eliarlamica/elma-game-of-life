# Any live cell with two or three live neighbours survives.
# Any dead cell with three live neighbours becomes a live cell.
# All other live cells die in the next generation. Similarly, all other dead cells stay dead.

#game_of_life_board_size = input("enter the board size?")

game_of_life_matrix = [
    ["0", "1", "0"],
    ["1", "0", "1"],
    ["0", "1", "1"]
]

for index, cell in enumerate(game_of_life_matrix):
    for index2, cell2 in enumerate(cell):
    if cell == "0":
        live_neighbour_cells = 0
        if game_of_life_matrix[0][1]

        #print(index, index2)
        #for game_of_life_matrix.cell[]

