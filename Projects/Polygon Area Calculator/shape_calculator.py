class Rectangle:
    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth 
    
    def set_width(self, new_width):
        self.width = new_width
    def set_height(self, new_heigth):
        self.heigth = new_heigth

    def get_area(self):
        return self.width * self.heigth
    
    def get_perimeter(self):
        return (2 * self.width + 2 * self.heigth)

    def get_diagonal(self):
        diagonal = ((self.width ** 2) + (self.heigth ** 2)) ** 0.5
        return diagonal 
    
    def get_picture(self):
        if self.heigth > 50 or self.width > 50:
            return "Too big for picture."
        picture = ""
        for line in range(0, self.heigth):
            picture += "*" * self.width
            picture += "\n"
        return picture
    
    def get_amount_inside(self, shape):
        area_shape = shape.get_area()
        this_area = self.get_area()
        fits_in = this_area // area_shape
        return fits_in 
    
    def __str__(self): # Figure how to discover object's class
        if self.__class__ == "Rectangle":
            return f"Rectangle(width={self.width}, height={self.heigth}"

class Square(Rectangle):
    def __init__(self, side):
        self.side = side 
        self.width = side 
        self.heigth = side 