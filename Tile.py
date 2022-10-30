import pygame
import Constants
import Board


class Piece:

    def __init__(self, color, row, column, king):
        self.color = color
        self.row = row
        self.column = column
        self.king = king
        self.selected = False

    def rangeX(self):
        return range(self.column * 100, (self.column * 100) + 100)

    def rangeY(self):
        return range(self.row * 100, (self.row * 100) + 100)

    def drawPiece(self):
        if self.color == "black":
            if self.row == 0:
                self.make_king()
        else:
            if self.row == 7:
                self.make_king()
        if self.color == "none":
            return None
        x_cord = (self.column * 100) + 50
        y_cord = (self.row * 100) + 50
        if self.selected == True:
            pygame.draw.rect(Constants.WIN, (118, 150, 150), [(self.column * 100), (self.row * 100), 100, 100])
        elif self.selected == False:
            pygame.draw.rect(Constants.WIN,(Constants.GREEN),[(self.column * 100), (self.row * 100), 100, 100])
        if self.color == "red":
            pygame.draw.circle(Constants.WIN, (150, 0, 0), (x_cord, y_cord), 40)
            pygame.draw.circle(Constants.WIN, Constants.BLACK, (x_cord, y_cord), 40, 1)
            pygame.draw.circle(Constants.WIN, (160, 0, 0), (x_cord, y_cord), 22.5)
            pygame.draw.circle(Constants.WIN, Constants.BLACK, (x_cord, y_cord), 22.5, 1)
        else:
            pygame.draw.circle(Constants.WIN, (90, 90, 90), (x_cord, y_cord), 40)
            pygame.draw.circle(Constants.WIN, Constants.BLACK, (x_cord, y_cord), 40, 1)
            pygame.draw.circle(Constants.WIN, (100, 100, 100), (x_cord, y_cord), 22.5)
            pygame.draw.circle(Constants.WIN, Constants.BLACK, (x_cord, y_cord), 22.5, 1)
        if self.king:
            pygame.draw.circle(Constants.WIN, (230, 175, 55), (x_cord, y_cord), 22.5)

    def isClicked(self,x,y):
        if x in self.rangeX() and y in self.rangeY():
            return True
        else:
            return False

    def switchSelection(self):
        if self.selected == False:
            self.selected = True
        else:
            self.selected = False

    def highlight(self,board):
        newBoard = board
        newBoard.pieces.remove(self)
        for i in newBoard.pieces:
            i.selected = False
        self.switchSelection()
        newBoard.pieces.insert(0,self)
        Board.drawBoard(newBoard.pieces)

    def make_king(self):
        return Piece(self.color, self.row, self.column, True)

### STANDARD BOARD
#red
piece1 = Piece("red",0,1,False)
piece2 = Piece("red",0,3,False)
piece3 = Piece("red",0,5,False)
piece4 = Piece("red",0,7,False)
piece5 = Piece("red",1,0,False)
piece6 = Piece("red",1,2,False)
piece7 = Piece("red",1,4,False)
piece8 = Piece("red",1,6,False)
piece9 = Piece("red",2,1,False)
piece10 = Piece("red",2,3,False)
piece11 = Piece("red",2,5,False)
piece12 = Piece("red",2,7,False)
#black
piece13 = Piece("black",5,0,False)
piece14 = Piece("black",5,2,False)
piece15 = Piece("black",5,4,False)
piece16 = Piece("black",5,6,False)
piece17 = Piece("black",6,1,False)
piece18 = Piece("black",6,3,False)
piece19 = Piece("black",6,5,False)
piece20 = Piece("black",6,7,False)
piece21 = Piece("black",7,0,False)
piece22 = Piece("black",7,2,False)
piece23 = Piece("black",7,4,False)
piece24 = Piece("black",7,6,False)

defaultPieces = [piece1,piece2,piece3,piece4,piece5,piece6,piece7,piece8,piece9,piece10,piece11,piece12,
                  piece13,piece14,piece15,piece16,piece17,piece18,piece19,piece20,piece21,piece22,piece23,piece24]


