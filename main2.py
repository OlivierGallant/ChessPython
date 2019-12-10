import numpy as np

class Piece():
    def __init__(self, piecetype, team):
        self.piecetype = piecetype
        self.team = team
    
    def getpiecetype(self):
        return self.piecetype
    
    def getteam(self):
        return self.team


class Board(Piece):

    def __init__(self):
        self.board = np.ndarray(shape=(8,8), dtype=object)
    
    def getpositionx(self, piece):
        positiony = 0
        while positiony < 8:
            positionx = 0
            if piece == board.getboardpiece(positionx, positiony):
                return positionx
            while positionx < 8:
                if piece == board.getboardpiece(positionx, positiony):
                    return positionx
                positionx += 1
            positiony += 1
            
    def getpositiony(self, piece):
        positiony = 0
        while positiony < 8:
            positionx = 0
            if piece == board.getboardpiece(positionx, positiony):
                return positiony
            while positionx < 8:
                if piece == board.getboardpiece(positionx, positiony):
                    return positiony
                positionx += 1
            positiony += 1

    def generateboardpieces(self, pieces):
        i = 0 
        while i < 8:
            self.board[i,1] = pieces[i]
            i += 1
        while 7 < i < 15:
            self.board[(i-8),6] = pieces[i]
            i += 1
        while 14 < i < 17:
            self.board[0,0] = pieces[i]
            self.board[7,0] = pieces[i+1]
            i += 2
        while 16 < i < 18:
            self.board[0,7] = pieces[i]
            self.board[7,7] = pieces[i+1]
            i += 2 
        while 18 < i < 21:
            self.board[1,0] = pieces[i]
            self.board[6,0] = pieces[i+1]
            i += 2
        while 20 < i < 23:
            self.board[1,7] = pieces[i]
            self.board[6,7] = pieces[i+1]
            i += 2
        while 22 < i < 25:
            self.board[2,0] = pieces[i]
            self.board[5,0] = pieces[i+1]
            i += 2
        while 24 < i < 27:
            self.board[2,7] = pieces[i]
            self.board[5,7] = pieces[i+1]
            i += 2
        while 26 < i < 28:
            self.board[5,0] = pieces[i]
            self.board[5,7] = pieces[i+1]
            i += 1 
        while 27 < i < 29:
            self.board[4,0] = pieces[i]
            self.board[4,7] = pieces[i+1]
            i += 1 
        
    def getboardpiece(self, locationx, locationy):
        return self.board[locationx, locationy]
    
    def setboardpiece(self, locationx, locationy, piece):
        self.board[locationx, locationy] = piece


    def movepiece(self, piece, positionx, positiony):
        currentpositionx = self.getpositionx(piece)
        currentpositiony = self.getpositiony(piece)
        temporarypiece = self.getboardpiece(currentpositionx, currentpositiony)
        self.setboardpiece(positionx, positiony, piece)
        self.setboardpiece(currentpositionx, currentpositiony, None)



def generatepieces():
    pieces = []
    i = 0
    while i < 8:
        pieces.append(Piece("pawn", 0))
        i += 1
    while 7 < i < 15:
        pieces.append(Piece("pawn", 1))
        i += 1
    while 14 < i < 17:
        pieces.append(Piece("rook", 0))
        i += 1
    while 16 < i < 19:
        pieces.append(Piece("rook", 1))
        i += 1
    while 18 < i < 21:
        pieces.append(Piece("bishop", 0))
        i += 1
    while 20 < i < 23:
        pieces.append(Piece("bishop", 1))
        i += 1 
    while 22 < i < 25:
        pieces.append(Piece("knight", 0))
        i += 1 
    while 24 < i < 27:
        pieces.append(Piece("knight", 1))
        i += 1
    while 26 < i < 28:
        pieces.append(Piece("king", 0))
        pieces.append(Piece("king", 1))
        i += 1 
    while 27 < i < 29:
        pieces.append(Piece("queen", 0))
        pieces.append(Piece("queen", 1))
        i += 1 
    return pieces

def debug(self):
    positiony = 0
    while positiony < 8:
        positionx = 0
        while positionx < 8:
            if self.getboardpiece(positionx, positiony) is not None:
                print("TYPE = " + self.getboardpiece(positionx, positiony).getpiecetype() + " Position x = " + str(positionx) + " Position y = " + str(positiony) + "TEAM = " + str(self.getboardpiece(positionx, positiony).getteam()))
            positionx += 1 
        positiony += 1 
        



pieces =  generatepieces()
board = Board()
board.generateboardpieces(pieces)
board.movepiece(board.getboardpiece(1,1), 1,5)
debug(board)

i = 0
while i < 29:
    print(pieces[i].getpiecetype())
    i += 1

