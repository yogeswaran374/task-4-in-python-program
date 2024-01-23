
'''create proper member variables inside the task if required and use them when necessary'''

class privatevariable:
    pi = 3.14
    radius = int(input("enter the number for radius : "))
    def area_of_circle(self):
        area = self.pi * self.radius * self.radius
        return area
    def perimeter_of_circle(self):
        perimeter = 2 * self.pi * self.radius
        return perimeter
    def display_pi(self):
        return self.pi
if __name__ == "__main__":    
   circle = privatevariable()
   print(circle.area_of_circle())
   print(circle.perimeter_of_circle())   
   print(circle.display_pi())
