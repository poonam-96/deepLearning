class Polygon:    #parent/base class
    __width= None     #bcz width and height are private so we cannot access it and we use get and set.
    __height= None
    
    def set_val(self, width,height):
        self.__width = width
        self.__height = height
    def get_width(self):         #bcz we can return only one value at a time, so we should wtite get for 
        return self.__width      #both height and width
    def get_height(self):
        return self.__height