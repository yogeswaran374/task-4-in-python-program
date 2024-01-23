'''calculate area and perimeter'''

class areaandperimeter:

    def __init__(self,a,l,b):
        self.a = a
        self.l = l
        self.b = b
    def area_of_square(self):
        area = self.a * self.a
        return area
    def perimeter_of_rectangle(self):
        perimeter = 2 * self.l * self.b
        return perimeter
   
    def __display_pi(self):
        return self.pi
if __name__ == "__main__":    
   a = int(input("enter the area 'a' number :" ))
   l = int(input("enter the length 'l' number :" ))
   b = int(input("enter the breadth 'b' number :" ))
   circle = areaandperimeter(a,l,b)
   print(circle.area_of_square())
   print(circle.perimeter_of_rectangle())
