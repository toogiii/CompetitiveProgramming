#Conway's game of life
def check_around(row,col,grid):
    cells_around = 0
    try:
        if grid[row + 1][col] == "1":
            cells_around += 1
        if grid[row + 1][col + 1] == "1":
            cells_around += 1
        if grid[row + 1][col - 1] == "1":
            cells_around += 1
        if grid[row][col + 1] == "1":
            cells_around += 1
        if grid[row][col - 1] == "1":
            cells_around += 1        
        if grid[row - 1][col] == "1":
            cells_around += 1        
        if grid[row - 1][col + 1] == "1":
            cells_around += 1
        if grid[row - 1][col - 1] == "1":
            cells_around += 1
    except:
        if row == 0 and col == 0:
            if grid[row][col + 1] == "1":
                cells_around += 1
            if grid[row + 1][col + 1] == "1":
                cells_around += 1
            if grid[row + 1][col]== "1":
                cells_around += 1
        elif row == 0 and col == 9:
            if grid[row][col - 1] == "1":
                cells_around += 1
            if grid[row + 1][col - 1] == "1":
                cells_around += 1
            if grid[row + 1][col] == "1": 
                cells_around += 1
        elif row == 9 and col == 9:
            if grid[row][col - 1] == "1":
                cells_around += 1
            if grid[row - 1][col - 1] == "1":
                cells_around += 1
            if grid[row - 1][col] == "1":
                cells_around += 1
        elif row == 9 and col == 0:
            if grid[row][col + 1] == "1":
                cells_around += 1
            if grid[row - 1][col + 1] == "1":
                cells_around += 1
            if grid[row - 1][col] == "1":
                cells_around += 1
        elif row == 0:
            if grid[row][col - 1] == "1":
                cells_around += 1
            if grid[row + 1][col + 1] == "1":
                cells_around += 1
            if grid[row + 1][col] == "1":
                cells_around += 1   
            if grid[row + 1][col - 1] == "1":
                cells_around += 1
            if grid[row][col + 1] == "1":
                cells_around += 1
        elif row == 9:
            if grid[row][col - 1] == "1":
                cells_around += 1
            if grid[row - 1][col + 1] == "1":
                cells_around += 1
            if grid[row - 1][col] == "1":
                cells_around += 1   
            if grid[row - 1][col - 1] == "1":
                cells_around += 1
            if grid[row][col + 1] == "1":
                cells_around += 1   
        elif col == 0:
            if grid[row][col + 1] == "1":
                cells_around += 1
            if grid[row + 1][col + 1] == "1":
                cells_around += 1
            if grid[row + 1][col] == "1":
                cells_around += 1   
            if grid[row - 1][col + 1] == "1":
                cells_around += 1
            if grid[row - 1][col] == "1":
                cells_around += 1
        elif col == 9:
            if grid[row][col - 1] == "1":
                cells_around += 1
            if grid[row + 1][col - 1] == "1":
                cells_around += 1
            if grid[row + 1][col] == "1":
                cells_around += 1   
            if grid[row - 1][col - 1] == "1":
                cells_around += 1
            if grid[row - 1][col] == "1": 
                cells_around += 1
    return cells_around
cases = int(input())
for case in range(cases):
    gens = int(input())
    lines = []
    storage = []
    for line in range(10):
        storage.append(list(input()))
    for generation in range(gens):
        lines = []
        for i in range(10):
            lines.append(list("0000000000"))        
        for row in range(10):
            for col in range(10):
                population = check_around(row, col, storage)
                if storage[row][col] == "1" and (population == 2 or population == 3):
                    lines[row][col] = "1"
                if storage[row][col] == "0" and population == 3:
                    lines[row][col] = "1"
        storage = lines.copy()
    for row in range(len(storage)):
        print("")
        for col in range(len(storage[row])):
            print(storage[row][col], end = "")
"""
1
3
0000000000
0000000000
0000000000
0000010000
0000111000
0000111000
0000010000
0000000000
0000000000
0000000000

0000000000
0000000000
0000000000
0000111000
0000111000
0000111000
0000111000
0000000000
0000000000
0000000000
"""