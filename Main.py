import pygame
import pygame.draw

import Board
import Tile
import Moving
import Moving2
import Moving3
import Constants

def play():
    Constants.WIN.fill(Constants.BEIGE)
    Board.newBoard()
    Board.drawBoard(Board.defaultBoard.pieces)
    board = Board.defaultBoard
    clock = pygame.time.Clock()
    kings = set()
    run = True
    while run == True:
        clock.tick(Constants.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if board.gameWon() == True:
                Board.winMessage(board.toMove())
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                for i in board.pieces:
                    if i.isClicked(mx,my) and i.color == board.toMove():
                        i.highlight(board)
                    if i.selected == True:
                        for j in Moving3.move(i,board,False,[],[]):
                            if mx in j.toMove[0] and my in j.toMove[1]:
                                pygame.draw.rect(Constants.WIN,(Constants.GREEN),[(i.column * 100),(i.row*100),100,100])
                                board.pieces.remove(i)
                                if i.color == "black" and int(j.toMove[1][0] / 100) == 0:
                                    kings.add(i)
                                elif i.color == "red" and int(j.toMove[1][0] / 100) == 7:
                                    kings.add(i)
                                if i in kings:
                                    newPiece = Tile.Piece(i.color,int(j.toMove[1][0] / 100),int(j.toMove[0][0] / 100),True)
                                    kings.add(newPiece)
                                else:
                                    newPiece = Tile.Piece(i.color, int(j.toMove[1][0] / 100), int(j.toMove[0][0] / 100),
                                                          False)
                                if j.toTake != []:
                                    for l in j.toTake:
                                        for k in board.pieces:
                                            if k.column == l[0] and k.row == l[1]:
                                                if k.color == "black":
                                                    board.num_black_pieces -= 1
                                                elif k.color == "red":
                                                    board.num_red_pieces -= 1
                                                pygame.draw.rect(Constants.WIN, (Constants.GREEN),
                                                                 [(k.column * 100), (k.row * 100), 100, 100])
                                                board.pieces.remove(k)
                                board.pieces.insert(0,newPiece)
                                Board.drawBoard(board.pieces)
                                board.num_moves += 1

        pygame.display.update()

    pygame.quit()

play()




