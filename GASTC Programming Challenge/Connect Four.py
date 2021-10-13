# Connect 4!
from my_game_lib import *

# 7x6 grid!

check_grid = [["E", "E", "E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E", "E", "E"]]

win = 0
f = 0

while not win > 0:
    
    # Player 1's Turn
    
    if f % 2 == 0:
        col = int(input("Please input what row you would like to put your chip in, Player 1 (starting from 0): "))
        row = 5
        for i in range(6):
            if check_grid[i][col] != "E":
                row = i - 1
                break
        check_grid[row][col] = "R"
        
    # Player 2's Turn
        
    else:
        col = int(input("Please input what row you would like to put your chip in, Player 2 (starting from 0): "))
        row = 5
        for j in range(6):
            if check_grid[j][col] != "E":
                row = j - 1
                break
        check_grid[row][col] = "W"
        
    # Check if Player 2 won
        
    if type(check_c4_board(check_grid, "W")) == str:
        print("Player 2 wins!")
        win = 1
        
    # Check if Player 1 won
    
    if type(check_c4_board(check_grid, "R")) == str:
        print("Player 1 wins!")
        win = 1
    
    # Print the grid
    
    print_grid(check_grid)
    f += 1