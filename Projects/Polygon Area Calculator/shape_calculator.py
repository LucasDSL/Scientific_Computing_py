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
        return f"Rectangle(width={self.width}, height={self.heigth})"

class Square(Rectangle):
    def __init__(self, side):
        self.width = side 
        self.heigth = side 
    
    def set_side(self, side):
        self.width = side
        self.heigth = side  
    def set_width(self, new_side):
        self.width = new_side
        self.heigth = new_side
    def set_heigth(self, new_side):
        self.width = new_side
        self.heigth = new_side
    
    def __str__(self):
        return f"Square(side={self.width})"
