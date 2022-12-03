''' DO NOT FORGET TO ADD COMMENTS '''

import numpy as np
from random import choice

class Fifteen:
    
    def __init__(self, size = 4):
        self.tiles = np.array([i for i in range(1,size**2)] + [0])
        self.adj = [[1,4], [0,2,5], [1,3,6], [2,7], [0,5,8], [1,4,6,9], [2,5,7,10], [3,6,11], [4,9,12], [5,8,10,13], [6,9,11,14], [7,10,15], [8,13], [9,12,14], [10,13,15], [11,14]]

    def update(self, move):
        if self.is_valid_move(move):
            self.transpose(move,0)
        
    def transpose(self, i, j):
        i = np.where(self.tiles == i)[0][0]
        j = np.where(self.tiles == j)[0][0]
        self.tiles[i], self.tiles[j] = self.tiles[j], self.tiles[i]

    def shuffle(self, steps=100):
        j = np.where(self.tiles == 0)[0][0]
        for i in range(100):
            i = choice(self.adj[j])
            self.tiles[i], self.tiles[j] = self.tiles[j], self.tiles[i]
            j = i

    def is_valid_move(self, move):
        i = np.where(self.tiles == move)[0][0]
        j = np.where(self.tiles == 0)[0][0]
        return i in self.adj[j]

    def is_solved(self):
        pass

    def draw(self):
        print("+---+----+---+----+")
        print("| 1 |  2 | 3 |  4 |")
        print("+---+----+---+----+")
        print("| 5 |  6 | 7 |  8 |")
        print("+---+----+---+----+")
        print("| 9 | 10 | 11| 12 |")
        print("+---+----+---+----+")
        print("|13 | 14 |15 |    |")
        print("+---+----+---+----+")

        
    def __str__(self):
        print("1 2 3 4")
        print("5 6 7 8")
        print("9 10 11 12")
        print("13 14 15  ")
    

if __name__ == '__main__':
    
    game = Fifteen()
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == False
    
    
    '''You should be able to play the game if you uncomment the code below'''
    '''
    game = Fifteen()
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')
    '''
    
    
        
