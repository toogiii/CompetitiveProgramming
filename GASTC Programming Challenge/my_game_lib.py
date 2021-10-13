def print_grid(grid):
    
    # Goes through each row and column of the grid and prints it line after line
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end = "")
        print("")


def check_ttt_board(board, char):
    
    # Down
    
    for i in range(len(board)):
        down = 0
        for j in range(len(board)):
            if board[j][i] == char:
                down += 1
            if down == 3:
                return char
    
    # Across
    
    for i in range(len(board)):
        across = 0
        for j in range(len(board[i])):
            if board[i][j] == char:
                across += 1
            if across == 3:
                return char
    
    # Diagonally
    
    if board[1][1] == char:
        if (board[0][0] == char and board[2][2] == char) or (board[0][2] == char and board[2][0] == char):
            return char
    
    return 0
        
def check_c4_board(board, char):
    
    # Down
    
    drow = 0
    for i in range(len(board)):
        down = 0
        for j in range(len(board)):
            if board[j][i] == char and (down == 0 or i == drow + 1):
                down += 1
            if down == 4:
                return char 
    
    # Across
    
    dcol = 0    
    for i in range(len(board)):
        across = 0
        for j in range(len(board)):
            if board[i][j] == char and (across == 0 or j == dcol + 1):
                dcol = j
                across += 1
            if across == 4:
                return char
    
    # Diagonally - accounts for both directions
    
    diag = 0
    drow = 0
    dcol = 0
    direction = 0    
    
    # Check board for each possible chip
    
    for i in range(42):
        diag = 0
        for row in range(len(board)):
            for col in range(len(board)):
                
                # First possible
                
                if board[row][col] == char and diag == 0:
                    diag += 1
                    drow = row
                    dcol = col
                
                # Figures direction of the diagonal    
                    
                if board[row][col] == char and row - 1 == drow and (col == dcol + 1 or col == dcol - 1) and diag == 1:
                    if col - 1 == dcol:
                        direction = -1
                    else:
                        direction = 1
                    diag += 1
                    drow = row
                    dcol = col
                    
                # Checks based on that direction
                    
                if board[row][col] == char and row - 1 == drow and col + direction == dcol:
                    diag += 1
                if diag == 3:  
                    return char
    return 0