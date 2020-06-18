from polygon import Polygon
from shape import Shape
class Square(Polygon, Shape):#to inherit the attribute , the functions we need to write the parent class name into 
    def area(self):  # the child class
        return self.get_width()*self.get_height()
    