def draw(grid):
    print("")
    print("1 2 3 4 5 6 7")
    print(" - - - - - - -")
    for row in grid:
        print(" ".join(str(cell) for cell in row))

def add_piece(grid, column, row, player):
    if player == 1:
        piece = "B"
    else:
        piece = "R"
    grid[row][column] = piece 
    return grid
    
# main program
board = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
won = False

draw(board)

player = 1


while not won:
    row_run = True
    print("It is player " + str(player) + "'s turn.")
    c_choice = int(input("Enter the column number (1-7):"))
    r_choice = 6
    while row_run:
        if board[r_choice][c_choice - 1] == 0:
            board = add_piece(board, c_choice - 1, r_choice , player)
            row_run = False
            
        else:
            r_choice = r_choice-1
        

    draw(board)

    # Check for a win condition (you need to implement this part)

    # Switch players
    if player == 1:
        player = 2
    else:
        player = 1

# Print the winning player
print("Player " + str(player) + " has won!")
input("Press enter to exit")