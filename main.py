import numpy
import math

class Pawn:
    def __init__(self, ide, position_x, position_y, team):
        self.id = ide
        self.pos_x = position_x
        self.pos_y = position_y
        self.team = team
        print("pawn generated")
    
    def getid(self):
        return self.id
    
    def getposx(self):
        return self.pos_x
    
    def getposy(self):
        return self.pos_y
    
    def getteam(self):
        return self.team

    def getrules(self):
        max_traveldistance_x = 1
        max_traveldistance_y = 0 
        max_traveldistance_x_y = math.sqrt(2)

class Rook:
    def __init__(self, ide, position_x, position_y, team):
        self.id = ide
        self.pos_x = position_x
        self.pos_y = position_y
        self.team = team
        print("rook generated")
    
    def getid(self):
        return self.id
    
    def getposx(self):
        return self.pos_x
    
    def getposy(self):
        return self.pos_y

    def getteam(self):
        return self.team

    def getrules(self):
        max_traveldistance_x = 1
        max_traveldistance_y = 0 
        max_traveldistance_x_y = math.sqrt(2)

class Castle:
    def __init__(self, ide, position_x, position_y, team):
        self.id = ide
        self.pos_x = position_x
        self.pos_y = position_y
        self.team = team
        print("castle generated")
    
    def getid(self):
        return self.id
    
    def getposx(self):
        return self.pos_x
    
    def getposy(self):
        return self.pos_y

    def getteam(self):
        return self.team

    def getrules(self):
        max_traveldistance_x = 1
        max_traveldistance_y = 0 
        max_traveldistance_x_y = math.sqrt(2)

class Bishop:
    def __init__(self, ide, position_x, position_y, team):
        self.id = ide
        self.pos_x = position_x
        self.pos_y = position_y
        self.team = team
        print("bishop generated")
    
    def getid(self):
        return self.id
    
    def getposx(self):
        return self.pos_x
    
    def getposy(self):
        return self.pos_y

    def getteam(self):
        return self.team

    def getrules(self):
        max_traveldistance_x = 1
        max_traveldistance_y = 0 
        max_traveldistance_x_y = math.sqrt(2)

class King:
    def __init__(self, ide, position_x, position_y, team):
        self.id = ide
        self.pos_x = position_x
        self.pos_y = position_y
        self.team = team
        print("king generated")
    
    def getid(self):
        return self.id
    
    def getposx(self):
        return self.pos_x
    
    def getposy(self):
        return self.pos_y

    def getteam(self):
        return self.team

    def getrules(self):
        max_traveldistance_x = 1
        max_traveldistance_y = 0 
        max_traveldistance_x_y = math.sqrt(2)

class Queen:
    def __init__(self, ide, position_x, position_y, team):
        self.id = ide
        self.pos_x = position_x
        self.pos_y = position_y
        self.team = team
        print("queen generated")
    
    def getid(self):
        return self.id
    
    def getposx(self):
        return self.pos_x
    
    def getposy(self):
        return self.pos_y

    def getteam(self):
        return self.team

    def getrules(self):
        max_traveldistance_x = 1
        max_traveldistance_y = 0 
        max_traveldistance_x_y = math.sqrt(2)




#GENERATE BOARD

def generatewhitepawns():
    i = 0
    p = []
    while i < 8:
        p.append(Pawn((i+1), (i+1), 2, 0))
        i += 1
    return p

def generateblackpawns():
    i = 0
    p = []
    while i < 8:
        p.append(Pawn((i+1), (i+1), 7, 1))
        i += 1
    return p

def generatewhiterooks():
    i = 0
    p = []
    p.append(Rook(1, 3, 1, 0)) 
    p.append(Rook(2, 6, 1, 0))     
    return p

def generateblackrooks():
    i = 0
    p = []
    p.append(Rook(1, 3, 8, 1))
    p.append(Rook(8, 6, 8, 1))     
    return p

def generatewhitecastles():
    i = 0
    p = []
    p.append(Castle(1, 1, 1, 0)) 
    p.append(Castle(2, 8, 1, 0))     
    return p

def generateblackcastles():
    i = 0
    p = []
    p.append(Castle(1, 1, 8, 1))
    p.append(Castle(8, 8, 8, 1))     
    return p

def generatewhitebishops():
    i = 0
    p = []
    p.append(Bishop(1, 2, 1, 0)) 
    p.append(Bishop(2, 7, 1, 0))     
    return p

def generateblackbishops():
    i = 0
    p = []
    p.append(Bishop(1, 2, 8, 1))
    p.append(Bishop(8, 7, 8, 1))     
    return p

def generatewhitekingqueen():
    i = 0
    p = []
    p.append(King(1, 5, 1, 0)) 
    p.append(Queen(2, 4, 1, 0))     
    return p

def generateblackkingqueen():
    i = 0
    p = []
    p.append(King(1, 5, 8, 1)) 
    p.append(Queen(2, 4, 8, 1))     
    return p



def debugpieces():
    i=0
    print("white pawns:")
    while i < 8:
        print("id ="+str(p_white[i].getid())+", pos x= "+str(p_white[i].getposx())+", pos y= "+str(p_white[i].getposy())+", team= "+str(p_white[i].getteam()))
        i+=1
    print("black pawns")
    i=0
    while i < 8:
        print("id ="+str(p_black[i].getid())+", pos x= "+str(p_black[i].getposx())+", pos y= "+str(p_black[i].getposy())+", team= "+str(p_black[i].getteam()))
        i+=1
    print("white rooks:")
    i=0
    while i < 2:
        print("id ="+str(r_white[i].getid())+", pos x= "+str(r_white[i].getposx())+", pos y= "+str(r_white[i].getposy())+", team= "+str(r_white[i].getteam()))
        i+=1
    print("black rooks:")
    i=0
    while i <2:
        print("id ="+str(r_black[i].getid())+", pos x= "+str(r_black[i].getposx())+", pos y= "+str(r_black[i].getposy())+", team= "+str(r_black[i].getteam()))
        i+=1

    print("white castles:")
    i=0
    while i < 2:
        print("id ="+str(c_white[i].getid())+", pos x= "+str(c_white[i].getposx())+", pos y= "+str(c_white[i].getposy())+", team= "+str(c_white[i].getteam()))
        i+=1

    print("black castles :")
    i=0
    while i <2:
        print("id ="+str(c_black[i].getid())+", pos x= "+str(c_black[i].getposx())+", pos y= "+str(c_black[i].getposy())+", team= "+str(c_black[i].getteam()))
        i+=1

    print("white bishops:")
    i=0
    while i < 2:
        print("id ="+str(b_white[i].getid())+", pos x= "+str(b_white[i].getposx())+", pos y= "+str(b_white[i].getposy())+", team= "+str(b_white[i].getteam()))
        i+=1

    print("black bishops:")
    i=0
    while i <2:
        print("id ="+str(b_black[i].getid())+", pos x= "+str(b_black[i].getposx())+", pos y= "+str(b_black[i].getposy())+", team= "+str(b_black[i].getteam()))
        i+=1
   

p_white = generatewhitepawns()
p_black = generateblackpawns()
r_white = generatewhiterooks()
r_black = generateblackrooks()
c_white = generatewhitecastles()
c_black = generateblackcastles()
b_white = generatewhitebishops()
b_black = generateblackbishops()


debugpieces()