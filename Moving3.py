import Tile

class Coords:

    def __init__(self,toMove,toTake):

        self.toMove = toMove
        self.toTake = toTake

#need sperate move and take function
#if not jumped then check for move and take
#if jumped then check for take with an updated piece and a piece removed from the board
#if it can jump 0 times only add the move coords
#if it can jump once add the move coords and the take coords
#if it can double jump add move coords take coords and double jump take coords

def blackMove(piece,board):

    coords = []
    isPieceLeft = False
    isPieceRight = False

    for i in board.pieces:

        #checks for piece to the left
        if i.column == piece.column - 1 and i.row == piece.row - 1 and piece.column - 1 > 0 and piece.row - 1 > 0:
            isPieceLeft = True

        #checks for piece to the right
        if i.column == piece.column + 1 and i.row == piece.row - 1 and piece.column + 1 < 7 and piece.row - 1 > 0:
            isPieceRight = True

    if isPieceLeft == False:
        coords.append(Coords((range(((piece.column - 1) * 100), (((piece.column - 1) * 100) + 100)),
                              range(((piece.row - 1) * 100), (((piece.row - 1) * 100) + 100))), []))

    if isPieceRight == False:
        coords.append(Coords((range(((piece.column + 1) * 100), (((piece.column + 1) * 100) + 100)),
                              range(((piece.row - 1) * 100), (((piece.row - 1) * 100) + 100))), []))

    return coords

def redMove(piece,board):

    coords = []
    isPieceLeft = False
    isPieceRight = False

    for i in board.pieces:

        #checks for piece to the left
        if piece.column > 0:
            if i.column == piece.column - 1 and i.row == piece.row + 1 and piece.column - 1 > 0 and piece.row + 1 < 7:
                isPieceLeft = True

        #checks for piece to the right
        if piece.column < 7:
            if i.column == piece.column + 1 and i.row == piece.row + 1 and piece.column + 1 < 7 and piece.row + 1 < 7:
                isPieceRight = True

    if isPieceLeft == False:
        coords.append(Coords((range(((piece.column - 1) * 100), (((piece.column - 1) * 100) + 100)),
                              range(((piece.row + 1) * 100), (((piece.row + 1) * 100) + 100))), []))

    if isPieceRight == False:
        coords.append(Coords((range(((piece.column + 1) * 100), (((piece.column + 1) * 100) + 100)),
                              range(((piece.row + 1) * 100), (((piece.row + 1) * 100) + 100))), []))

    return coords

def blackTakeLeft(piece,board):

    coords = []
    isPieceLeft = False
    canTakeLeft = True

    for i in board.pieces:

        #checks for piece to the left
        if i.column == piece.column - 1 and i.row == piece.row - 1 and piece.column - 1 > 0 and piece.row - 1 > 0:
            isPieceLeft = True

    if isPieceLeft == True:
        for i in board.pieces:
            if i.column == piece.column - 2 and i.row == piece.row - 2 and piece.column - 2 > 0 and piece.row - 2 > 0:
                canTakeLeft = False
        if canTakeLeft == True:
            coords.append(Coords((range(((piece.column - 2) * 100), (((piece.column - 2) * 100) + 100)),
                                  range(((piece.row - 2) * 100), (((piece.row - 2) * 100) + 100))),
                                 [(piece.column - 1, piece.row - 1)]))

    return coords

def blackTakeRight(piece,board):

    coords = []
    isPieceRight = False
    canTakeRight = True

    for i in board.pieces:
        if i.column == piece.column + 1 and i.row == piece.row - 1 and piece.column + 1 < 7 and piece.row - 1 > 0:
            isPieceRight = True

    if isPieceRight == True:
        for i in board.pieces:
            if i.column == piece.column + 2 and i.row == piece.row - 2 and piece.column + 2 < 7 and piece.row - 2 > 0:
                canTakeRight = False
        if canTakeRight == True:
            coords.append(Coords((range(((piece.column + 2) * 100), (((piece.column + 2) * 100) + 100)),
                                  range(((piece.row - 2) * 100), (((piece.row - 2) * 100) + 100))),
                                 [(piece.column + 1, piece.row - 1)]))

    return coords


def redTakeLeft(piece,board):

    coords = []
    isPieceLeft = False
    canTakeLeft = True

    for i in board.pieces:

        # checks for piece to the left
        if i.column == piece.column - 1 and i.row == piece.row + 1 and piece.column - 1 > 0 and piece.row + 1 < 7:
            isPieceLeft = True

    if isPieceLeft == True:
        for i in board.pieces:
            if i.column == piece.column - 2 and i.row == piece.row + 2 and piece.column - 2 > 0 and piece.row + 2 < 7:
                canTakeLeft = False
        if canTakeLeft == True:
            coords.append(Coords((range(((piece.column - 2) * 100), (((piece.column - 2) * 100) + 100)),
                                  range(((piece.row + 2) * 100), (((piece.row + 2) * 100) + 100))),
                                 [(piece.column - 1, piece.row + 1)]))

    return coords

def redTakeRight(piece,board):

    coords = []
    isPieceRight = False
    canTakeRight = True

    for i in board.pieces:
        if i.column == piece.column + 1 and i.row == piece.row + 1 and piece.column + 1 < 7 and piece.row + 1 < 7:
            isPieceRight = True

    if isPieceRight == True:
        for i in board.pieces:
            if i.column == piece.column + 2 and i.row == piece.row + 2 and piece.column + 2 < 7 and piece.row + 2 < 7:
                canTakeRight = False
        if canTakeRight == True:
            coords.append(Coords((range(((piece.column + 2) * 100), (((piece.column + 2) * 100) + 100)),
                                  range(((piece.row + 2) * 100), (((piece.row + 2) * 100) + 100))),
                                 [(piece.column + 1, piece.row + 1)]))

    return coords

def kingMove(piece,board):

    coords = []
    UL = Coords((range(((piece.column - 1) * 100), (((piece.column - 1) * 100) + 100)),
                              range(((piece.row - 1) * 100), (((piece.row - 1) * 100) + 100))), [])
    UR = Coords((range(((piece.column + 1) * 100), (((piece.column + 1) * 100) + 100)),
                              range(((piece.row - 1) * 100), (((piece.row - 1) * 100) + 100))), [])
    DL = Coords((range(((piece.column - 1) * 100), (((piece.column - 1) * 100) + 100)),
                              range(((piece.row + 1) * 100), (((piece.row + 1) * 100) + 100))), [])
    DR = Coords((range(((piece.column + 1) * 100), (((piece.column + 1) * 100) + 100)),
                              range(((piece.row + 1) * 100), (((piece.row + 1) * 100) + 100))), [])
    JUL = Coords((range(((piece.column - 2) * 100), (((piece.column - 2) * 100) + 100)),
                                  range(((piece.row - 2) * 100), (((piece.row - 2) * 100) + 100))),
                                 [(piece.column - 1, piece.row - 1)])
    JUR = Coords((range(((piece.column + 2) * 100), (((piece.column + 2) * 100) + 100)),
                                  range(((piece.row - 2) * 100), (((piece.row - 2) * 100) + 100))),
                                 [(piece.column + 1, piece.row - 1)])
    JDL = Coords((range(((piece.column - 2) * 100), (((piece.column - 2) * 100) + 100)),
                                  range(((piece.row + 2) * 100), (((piece.row + 2) * 100) + 100))),
                                 [(piece.column - 1, piece.row + 1)])
    JDR = Coords((range(((piece.column + 2) * 100), (((piece.column + 2) * 100) + 100)),
                                  range(((piece.row + 2) * 100), (((piece.row + 2) * 100) + 100))),
                                 [(piece.column + 1, piece.row + 1)])
    JULUL = Coords((range(((piece.column - 4) * 100), (((piece.column - 4) * 100) + 100)),
                                  range(((piece.row - 4) * 100), (((piece.row - 4) * 100) + 100))),
                                 [(piece.column - 1, piece.row - 1),(piece.column - 3, piece.row - 3)])
    JURUR = Coords((range(((piece.column + 4) * 100), (((piece.column + 4) * 100) + 100)),
                                  range(((piece.row - 4) * 100), (((piece.row - 4) * 100) + 100))),
                                 [(piece.column + 1, piece.row - 1),(piece.column + 3, piece.row - 3)])
    JDLDL = Coords((range(((piece.column - 4) * 100), (((piece.column - 4) * 100) + 100)),
                    range(((piece.row + 4) * 100), (((piece.row + 4) * 100) + 100))),
                   [(piece.column - 1, piece.row + 1), (piece.column - 3, piece.row + 3)])
    JDRDR = Coords((range(((piece.column + 4) * 100), (((piece.column + 4) * 100) + 100)),
                    range(((piece.row + 4) * 100), (((piece.row + 4) * 100) + 100))),
                   [(piece.column + 1, piece.row + 1), (piece.column + 3, piece.row + 3)])
    JULUR = Coords((range(((piece.column - 0) * 100), (((piece.column - 0) * 100) + 100)),
                                  range(((piece.row - 4) * 100), (((piece.row - 4) * 100) + 100))),
                                 [(piece.column - 1, piece.row - 1),(piece.column - 1, piece.row - 3)])
    JURUL = Coords((range(((piece.column - 0) * 100), (((piece.column - 0) * 100) + 100)),
                                  range(((piece.row - 4) * 100), (((piece.row - 4) * 100) + 100))),
                                 [(piece.column + 1, piece.row - 1),(piece.column + 1, piece.row - 3)])
    JDLDR = Coords((range(((piece.column - 0) * 100), (((piece.column - 0) * 100) + 100)),
                                  range(((piece.row + 4) * 100), (((piece.row + 4) * 100) + 100))),
                                 [(piece.column - 1, piece.row + 1),(piece.column - 1, piece.row + 3)])
    JDRDL = Coords((range(((piece.column - 0) * 100), (((piece.column - 0) * 100) + 100)),
                                  range(((piece.row + 4) * 100), (((piece.row + 4) * 100) + 100))),
                                 [(piece.column + 1, piece.row + 1),(piece.column + 1, piece.row + 3)])
    JULDL = Coords((range(((piece.column - 4) * 100), (((piece.column - 4) * 100) + 100)),
                                  range(((piece.row - 0) * 100), (((piece.row - 0) * 100) + 100))),
                                 [(piece.column - 1, piece.row - 1),(piece.column - 3, piece.row - 1)])
    JURDR = Coords((range(((piece.column + 4) * 100), (((piece.column + 4) * 100) + 100)),
                                  range(((piece.row - 0) * 100), (((piece.row - 0) * 100) + 100))),
                                 [(piece.column + 1, piece.row - 1),(piece.column + 3, piece.row - 1)])
    JDLUL = Coords((range(((piece.column - 4) * 100), (((piece.column - 4) * 100) + 100)),
                                  range(((piece.row - 0) * 100), (((piece.row - 0) * 100) + 100))),
                                 [(piece.column - 1, piece.row + 1),(piece.column - 3, piece.row + 1)])
    JDRUR = Coords((range(((piece.column + 4) * 100), (((piece.column + 4) * 100) + 100)),
                                  range(((piece.row - 0) * 100), (((piece.row - 0) * 100) + 100))),
                                 [(piece.column + 1, piece.row + 1),(piece.column + 3, piece.row + 1)])

    canUL = False
    canUR = False
    canDL = False
    canDR = False
    canJUL = False
    canJUR = False
    canJDL = False
    canJDR = False
    canJULUL = False
    canJURUR = False
    canJDLDL = False
    canJDRDR = False
    canJULUR = False
    canJURUL = False
    canJDLDR = False
    canJDRDL = False
    canJULDL = False
    canJURDR = False
    canJDLUL = False
    canJDRUR = False

    isPieceUL = False
    isPieceUR = False
    isPieceDL = False
    isPieceDR = False
    isPieceU2L2 = False
    isPieceU2R2 = False
    isPieceD2L2 = False
    isPieceD2R2 = False
    isPieceU3L3 = False
    isPieceU4L4 = False
    isPieceU3R3 = False
    isPieceU4R4 = False
    isPieceD3L3 = False
    isPieceD4L4 = False
    isPieceD3R3 = False
    isPieceD4R4 = False
    isPieceU3L1 = False
    isPieceU3R1 = False
    isPieceU4 = False
    isPieceD3L1 = False
    isPieceD3R1 = False
    isPieceD4 = False
    isPieceU1L3 = False
    isPieceD1L3 = False
    isPieceL4 = False
    isPieceU1R3 = False
    isPieceD1R3 = False
    isPieceR4 = False


    if piece.row > 0 and piece.column > 0:
        canUL = True
        if piece.row > 1 and piece.column > 1:
            canJUL = True
            if piece.row > 3 and piece.column > 3:
                canJULUL = True
            if piece.row > 3 and piece.column > 1:
                canJULUR = True
            if piece.row > 1 and piece.column > 3:
                canJULDL = True
    if piece.row > 0 and piece.column < 7:
        canUR = True
        if piece.row > 1 and piece.column < 6:
            canJUR = True
            if piece.row > 3 and piece.column < 4:
                canJURUR = True
            if piece.row > 3 and piece.column < 6:
                canJURUL = True
            if piece.row > 1 and piece.column < 4:
                canJURDR = True
    if piece.row < 7 and piece.column > 0:
        canDL = True
        if piece.row < 6 and piece.column > 1:
            canJDL = True
            if piece.row < 4 and piece.column > 3:
                canJDLDL = True
            if piece.row < 4 and piece.column > 1:
                canJDLDR = True
            if piece.row < 6 and piece.column > 3:
                canJDLUL = True
    if piece.row < 7 and piece.column < 7:
        canDR = True
        if piece.row < 6 and piece.column < 6:
            canJDR = True
            if piece.row < 4 and piece.column < 4:
                canJDRDR = True
            if piece.row < 4 and piece.column < 6:
                canJDRDL = True
            if piece.row < 6 and piece.column < 4:
                canJDRUR = True

    for i in board.pieces:
        if i.row == piece.row - 1 and i.column == piece.column - 1:
            isPieceUL = True
        elif i.row == piece.row - 1 and i.column == piece.column + 1:
            isPieceUR = True
        elif i.row == piece.row + 1 and i.column == piece.column - 1:
            isPieceDL = True
        elif i.row == piece.row + 1 and i.column == piece.column + 1:
            isPieceDR = True
        elif i.row == piece.row - 2 and i.column == piece.column - 2:
            isPieceU2L2 = True
        elif i.row == piece.row - 2 and i.column == piece.column + 2:
            isPieceU2R2 = True
        elif i.row == piece.row + 2 and i.column == piece.column - 2:
            isPieceD2L2 = True
        elif i.row == piece.row + 2 and i.column == piece.column + 2:
            isPieceD2R2 = True
        elif i.row == piece.row - 3 and i.column == piece.column - 3:
            isPieceU3L3 = True
        elif i.row == piece.row - 4 and i.column == piece.column - 4:
            isPieceU4L4 = True
        elif i.row == piece.row - 3 and i.column == piece.column + 3:
            isPieceU3R3 = True
        elif i.row == piece.row - 4 and i.column == piece.column + 4:
            isPieceU4R4 = True
        elif i.row == piece.row + 3 and i.column == piece.column - 3:
            isPieceD3L3 = True
        elif i.row == piece.row + 4 and i.column == piece.column - 4:
            isPieceD4L4 = True
        elif i.row == piece.row + 3 and i.column == piece.column + 3:
            isPieceD3R3 = True
        elif i.row == piece.row + 4 and i.column == piece.column + 4:
            isPieceD4R4 = True
        elif i.row == piece.row - 3 and i.column == piece.column - 1:
            isPieceU3L1 = True
        elif i.row == piece.row - 3 and i.column == piece.column + 1:
            isPieceU3R1 = True
        elif i.row == piece.row - 4 and i.column == piece.column:
            isPieceU4 = True
        elif i.row == piece.row + 3 and i.column == piece.column - 1:
            isPieceD3L1 = True
        elif i.row == piece.row + 3 and i.column == piece.column + 1:
            isPieceD3R1 = True
        elif i.row == piece.row + 4 and i.column == piece.column:
            isPieceD4 = True
        elif i.row == piece.row - 1 and i.column == piece.column - 3:
            isPieceU1L3 = True
        elif i.row == piece.row + 1 and i.column == piece.column - 3:
            isPieceD1L3 = True
        elif i.row == piece.row and i.column == piece.column - 4:
            isPieceL4 = True
        elif i.row == piece.row - 1 and i.column == piece.column + 3:
            isPieceU1R3 = True
        elif i.row == piece.row + 1 and i.column == piece.column + 3:
            isPieceD1R3 = True
        elif i.row == piece.row and i.column == piece.column + 4:
            isPieceR4 = True

    #regular moves
    if isPieceUL == False and canUL == True:
        coords.append(UL)
    if isPieceUR == False and canUR == True:
        coords.append(UR)
    if isPieceDL == False and canDL == True:
        coords.append(DL)
    if isPieceDR == False and canDR == True:
        coords.append(DR)

    #single jumps
    if isPieceUL == True and isPieceU2L2 == False and canJUL == True:
        coords.append(JUL)
    if isPieceUR == True and isPieceU2R2 == False and canJUR == True:
        coords.append(JUR)
    if isPieceDL == True and isPieceD2L2 == False and canJDL == True:
        coords.append(JDL)
    if isPieceDR == True and isPieceD2R2 == False and canJDR == True:
        coords.append(JDR)

    #double jumps one direction
    if isPieceUL == True and isPieceU2L2 == False and isPieceU3L3 == True and isPieceU4L4 == False and canJULUL == True:
        coords.append(JULUL)
    if isPieceUR == True and isPieceU2R2 == False and isPieceU3R3 == True and isPieceU4R4 == False and canJURUR == True:
        coords.append(JURUR)
    if isPieceDL == True and isPieceD2L2 == False and isPieceD3L3 == True and isPieceD4L4 == False and canJDLDL == True:
        coords.append(JDLDL)
    if isPieceDR == True and isPieceD2R2 == False and isPieceD3R3 == True and isPieceD4R4 == False and canJDRDR == True:
        coords.append(JDRDR)

    #vertical double jumps
    if isPieceUL == True and isPieceU2L2 == False and isPieceU3L1 == True and isPieceU4 == False and canJULUR == True:
        coords.append(JULUR)
    if isPieceUR == True and isPieceU2R2 == False and isPieceU3R1 == True and isPieceU4 == False and canJURUL == True:
        coords.append(JURUL)
    if isPieceDL == True and isPieceD2L2 == False and isPieceD3L1 == True and isPieceD4 == False and canJDLDR == True:
        coords.append(JDLDR)
    if isPieceDR == True and isPieceD2R2 == False and isPieceD3R1 == True and isPieceD4 == False and canJDRDL == True:
        coords.append(JDRDL)

    #horizontal double jumps
    if isPieceUL == True and isPieceU2L2 == False and isPieceU1L3 == True and isPieceL4 == False and canJULDL == True:
        coords.append(JULDL)
    if isPieceUR == True and isPieceU2R2 == False and isPieceU1R3 == True and isPieceR4 == False and canJURDR == True:
        coords.append(JURDR)
    if isPieceDL == True and isPieceD2L2 == False and isPieceD1L3 == True and isPieceL4 == False and canJDLUL == True:
        coords.append(JDLUL)
    if isPieceDR == True and isPieceD2R2 == False and isPieceD1R3 == True and isPieceR4 == False and canJDRUR == True:
        coords.append(JDRUR)

    return coords


def move(piece,board,jumped,listCoords,takenPiece):

    coords = listCoords

    if piece.king:

        coords = kingMove(piece,board)


    elif not piece.king:

        if jumped == False:

            if piece.color == "black":
                if blackMove(piece,board) != []:
                        coords.append(blackMove(piece,board))
                coords = blackMove(piece,board)
                if blackTakeLeft(piece,board) != []:
                    for i in blackTakeLeft(piece,board):
                        coords.append(i)
                    move(Tile.Piece(piece.color, piece.row - 2, piece.column - 2, piece.king),board,True,coords,
                         (piece.column - 1, piece.row - 1))
                if blackTakeRight(piece,board) != []:
                    for i in blackTakeRight(piece,board):
                        coords.append(i)
                    move(Tile.Piece(piece.color, piece.row - 2, piece.column + 2, piece.king), board, True, coords,
                         (piece.column + 1, piece.row - 1))

            if piece.color == "red":
                if coords == []:
                    coords = redMove(piece,board)
                else:
                    coords.append(redMove(piece,board))
                if redTakeLeft(piece,board) != []:
                    for i in redTakeLeft(piece,board):
                        coords.append(i)
                    move(Tile.Piece(piece.color, piece.row + 2, piece.column - 2, piece.king), board, True, coords,
                         (piece.column - 1, piece.row + 1))
                if redTakeRight(piece,board) != []:
                    for i in redTakeRight(piece,board):
                        coords.append(i)
                    move(Tile.Piece(piece.color, piece.row + 2, piece.column + 2, piece.king), board, True, coords,
                         (piece.column + 1, piece.row + 1))

        else:

            if piece.color == "black" or piece.king:

                if blackTakeLeft(piece,board) != []:
                    for i in blackTakeLeft(piece,board):
                        coords.append(i)
                    coords[-1].toTake.append(takenPiece)
                if blackTakeRight(piece,board) != []:
                    for i in blackTakeRight(piece,board):
                        coords.append(i)
                    coords[-1].toTake.append(takenPiece)

            if piece.color == "red" or piece.king:

                if redTakeLeft(piece,board) != []:
                    for i in redTakeLeft(piece,board):
                        coords.append(i)
                    coords[-1].toTake.append(takenPiece)
                if redTakeRight(piece,board) != []:
                    for i in redTakeRight(piece,board):
                        coords.append(i)
                    coords[-1].toTake.append(takenPiece)

    return coords

