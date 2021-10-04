import random

class Ship():
    def __init__(self, name, size):
        self.name = name
        self.size =size         
        

class Board():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def place_ship(ship):
        row = random.randint(0,9)
        col = random.randint(0,9)
        indexes = [[row, col]]
        for i in range(0,ship.size):
            indexes.append([col, i])
        return indexes
    
    def create_board(self):
        grid = []
        for x in range(self.width):
            row = []
            for y in range(self.height):
                row.append('0')
            grid.append(row)
        for ship in ships:
            indexes = self.place_ship(ship)
            for index in indexes:
                board[index[0]][index[1]] = "S"


carrier = Ship("carrier", 5)
battleship = Ship("battleship",4)
cruiser = Ship("cruiser",3)
submarine = Ship("submarine",3)
destroyer = Ship("destroyer", 2)

grid = Board(10,10)
grid = grid.create_board(10, 10)

ships = [carrier, battleship, cruiser, submarine, destroyer]

moves = []

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
    
user_input()

