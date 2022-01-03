import math
class Vector2D(object):
    'Simple python for Vector 2D'
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        # kembalikan (a,b) + (c,d) = (a+c,b+d)
        return Vector2D(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        # kembalikan (a,b) - (c,d) = (a-c,b-d)
        return Vector2D(self.x-other.x,self.y-other.y)
        #berhenti disini
    def __mul__(self,other):
        #(a,b) * (c,d) = (a*c,b*d)
        return Vector2D(self.x*other.x,self.y*other.y)
        #berhenti disini
    def __abs__(self):
        # kembalikan ||a,b|| = akar((a,b) * (a,b)), atau
        # akar(a pangkat 2+b pangkat 2), gunakan math.sqrt
        return Vector2D (int(math.sqrt((self.x)**2)),int(math.sqrt((self.y)**2)))
        #-3**2 = 9
        #berhenti disini
    def __eq__(self,other):
        return((self.x==other.x) and (self.y==other.y))
        #berhenti disini
    def __str__(self) -> str:
        return str(self.x)+','+str(self.y)
    