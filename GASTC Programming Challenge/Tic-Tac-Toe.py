# Tic-Tac-Toe!
from my_game_lib import *

# 3x3 grid:

check_grid = [["E" ,"E" ,"E"], ["E" ,"E" ,"E"], ["E" ,"E" ,"E"]]

# Checks to see who won

win = 0

# Checks who's turn it is

f = 0

while not win > 0:
    
    # Player 1's Turn
    
    if f % 2 == 0:
        row = int(input("Please input what row you would like to an X in, Player 1 (starting from 0): "))
        col = int(input("Please input what column you would like to an X in, Player 1 (starting from 0): "))
        check_grid[row][col] = "X"
        
    # Player 2's Turn
        
    else:
        row = int(input("Please input what row you would like to put an O in, Player 2 (starting from 0): "))
        col = int(input("Please input what column you would like to an X in, Player 1 (starting from 0): "))
        check_grid[row][col] = "O"
        
    # Check if Player 2 won
        
    if type(check_ttt_board(check_grid, "O")) == str:
        print("Player 2 wins!")
        win = 1
        
    # Check if Player 1 won
    
    if type(check_ttt_board(check_grid, "X")) == str:
        print("Player 1 wins!")
        win = 1
    
    # Print the grid
    
    print_grid(check_grid)
    f += 1