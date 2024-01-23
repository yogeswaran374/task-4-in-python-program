'''create python class called circle with constructor which will take a list as an argument for the task.
the list is [10,501,22,37,100,999,87,351]'''

class circle:
    pi = 3.14

    def __init__(self, r):

        self.a = r[0]
        self.b = r[1]
        self.c = r[2]
        self.d = r[3]
        self.e = r[4]
        self.f = r[5]
        self.g = r[6]
        self.h = r[7]

    def area_of_circle0(self):
        area = self.pi * self.a *self.a
        return area
    def area_of_circle1(self):
        area = self.pi * self.b *self.b
        return area
    def area_of_circle2(self):
        area = self.pi * self.c *self.c
        return area
    def area_of_circle3(self):
        area = self.pi * self.d *self.d
        return area
    def area_of_circle4(self):
        area = self.pi * self.e *self.e
        return area
    def area_of_circle5(self):
        area = self.pi * self.f *self.f
        return area
    def area_of_circle6(self):
        area = self.pi * self.g *self.g
        return area
    def area_of_circle7(self):
        area = self.pi * self.h *self.h
        return area
    
if __name__ =="__main__":

    r = [10,501,22,37,100,999,87,351]
    c = circle(r)
    print("area of circle0 : ",c.area_of_circle0())
    print("area of circle1 : ",c.area_of_circle1())
    print("area of circle2 : ",c.area_of_circle2())
    print("area of circle3 : ",c.area_of_circle3())
    print("area of circle4 : ",c.area_of_circle4())
    print("area of circle5 : ",c.area_of_circle5())
    print("area of circle6 : ",c.area_of_circle6())
    print("area of circle7 : ",c.area_of_circle7())


   
        

