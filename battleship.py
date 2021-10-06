import random


class Ship():
    def __init__(self, name, size):
        self.name = name
        self.size =size         
        

class Board():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def place_ship(self, ship):
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
                grid[index[0]][index[1]] = "S"
        
        return grid

ships = [Ship("carrier", 5), Ship("battleship",4), Ship("cruiser",3), Ship("submarine",3), Ship("destroyer", 2)]

board = Board(10,10)
board = board.create_board()

moves = []

def user_input():
    count = 0
    while count < 10:
        column = input("Please choose a column number 1-10 ")
        row = input("Please choose a row number 1-10 ")
        moves.append([column,row])
        count+=1
        if board[row-1][column-1] == "S":
            board[row-1][column-1] = "S/X"
            print "Hit!"
        else:
            print "Miss!"
            board[row-1][column-1] = "X"
        print("--------------")
        print"Moves remaining: ", 10-count
        print "Moves: ", moves
        print("--------------")
    
    for row in board:
        print row
    
user_input()

