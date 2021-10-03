import random

ships = {
    "carrier": 5,
    "battleship": 4,
    "cruiser": 3,
    "submarine": 3,
    "destroyer": 2
}

moves = []

def random_row(grid):
    return randint(0, len(board) - 1)
def random_col(grid):
    return randint(0, len(board[0]) - 1)


def place_ship(ship):
    row = random.randint(0,9)
    col = random.randint(0,9)
    indexes = [[row, col]]
    for i in range(0,ship[1]):
        indexes.append([col, i])
    return indexes

def initialize_board(board_width, board_height):
    grid = []
    for x in range(board_width):
        row = []
        for y in range(board_height):
            row.append('0')
        grid.append(row)
    for ship in ships.items():
        indexes = place_ship(ship)
        for index in indexes:
            grid[index[0]][index[1]] = "S"
    return grid

def user_input():
    count = 0
    while count < 10:
        column = input("Please choose a column number 1-10 ")
        row = input("Please choose a row number 1-10 ")
        moves.append([column,row])
        count+=1
        if grid[row-1][column-1] == "S":
            grid[row-1][column-1] = "S/X"
            print "Hit!"
        else:
            print "Miss!"
            grid[row-1][column-1] = "X"
        print("--------------")
        print"Moves remaining: ", 10-count
        print "Moves: ", moves
        print("--------------")
    
    for row in grid:
        print row
    
grid = initialize_board(10, 10)
user_input()

