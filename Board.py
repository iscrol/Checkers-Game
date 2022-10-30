import pygame
import Constants
import Moving
import Tile


class Board():

     def __init__(self, pieces, num_moves, num_black_pieces, num_red_pieces):
         self.pieces = pieces
         self.num_moves = num_moves
         self.num_black_pieces = num_black_pieces
         self.num_red_pieces = num_red_pieces

     #returns whose turn it is
     def toMove(self):
         if self.num_moves % 2 == 0:
             return 'black'
         return 'red'


     def gameWon(self):
        if self.num_red_pieces == 0 or self.num_black_pieces == 0:
            return True
        else:
            return False
        '''else:
            if self.toMove() == "black":
                for i in self.pieces:
                    if i.color == "black":
                        if Moving.moveCoords(i,self) != [] or Moving.takeCoords(i,self, i.column, i.row) != []:
                            return False
            elif self.toMove() == "red":
                for i in self.pieces:
                    if i.color == "red":
                        if Moving.moveCoords(i, self) != [] or Moving.takeCoords(i, self, i.column, i.row) != []:
                            return False
            return True'''



def newBoard():
    i = 0
    while i < 8:
        j = 0
        if i%2 == 0:
            j = 1
        else:
            j = 0
        while j < 8:
            pygame.draw.rect(Constants.WIN,(Constants.GREEN),[(i*100),(j*100),100,100])
            j += 2
        i += 1

def drawBoard(pieces):
    for i in pieces:
        if i.color == "black":
            if i.row == 0:
                i.make_king()
        else:
            if i.row == 7:
                i.make_king()
        i.drawPiece()

defaultBoard = Board(Tile.defaultPieces,0,12,12)

def winMessage(color):
    if color == "black":
        message = Constants.FONT.render("Red won the game!", True, (150,0,0))
    elif color == "red":
        message = Constants.FONT.render("Black won the game!", True, "black")
    text_rect = message.get_rect(center=(400, 400))
    Constants.WIN.blit(message, text_rect)