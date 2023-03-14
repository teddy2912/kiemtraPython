import math
from Shape import Shape


class Circle(Shape):
    def __init__(self,x,y,banKinh): 
        super().__init__(x,y)
        self.banKinh = banKinh

    def chuVi(banKinh):
        chuVi = 2 * math.pi * banKinh
        return chuVi
    def dineTich(banKinh):
        dienTich = banKinh * banKinh * math.pi
        return dienTich