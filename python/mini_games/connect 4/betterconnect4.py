def check_win(grid):
    # Check horizontal
    for row in grid:
        for i in range(len(row) - 3):
            if row[i] == row[i + 1] == row[i + 2] == row[i + 3] != 0:
                return True

    # Check vertical
    for col in range(len(grid[0])):
        for i in range(len(grid) - 3):
            if grid[i][col] == grid[i + 1][col] == grid[i + 2][col] == grid[i + 3][col] != 0:
                return True

    # Check diagonal (from top-left to bottom-right)
    for row in range(len(grid) - 3):
        for col in range(len(grid[0]) - 3):
            if grid[row][col] == grid[row + 1][col + 1] == grid[row + 2][col + 2] == grid[row + 3][col + 3] != 0:
                return True

    # Check diagonal (from bottom-left to top-right)
    for row in range(3, len(grid)):
        for col in range(len(grid[0]) - 3):
            if grid[row][col] == grid[row - 1][col + 1] == grid[row - 2][col + 2] == grid[row - 3][col + 3] != 0:
                return True

    return False

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
    r_choice = 5
    while row_run:
        if board[r_choice][c_choice - 1] == 0:
            board = add_piece(board, c_choice - 1, r_choice , player)
            row_run = False
        else:
            r_choice = r_choice-1

    draw(board)

    # Check for a win condition
    won = check_win(board)

    # Switch players
    if player == 1:
        player = 2
    else:
        player = 1

# Print the winning player
print("Player " + str(player) + " has won!")
input("Press enter to exit")