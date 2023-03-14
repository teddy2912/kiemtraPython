import math
from Shape import Shape

class Rect(Shape):
    def __init__(self ,x,y,a,b,c): 
        super().__init__(x,y)
        self.a = a
        self.b = b
        self.c = c

def chuVi(a,b,c):
    chuVi = a + b + c
    return chuVi
    
def dienTich(a,b,c,chuVi):
    p = chuVi / 2
    dienTich = math.sqrt(p* (p-a) * (p-b) * (p-c))
    return dienTich