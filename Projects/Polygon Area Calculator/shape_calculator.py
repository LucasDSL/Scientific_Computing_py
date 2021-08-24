class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height 
    
    def set_width(self, new_width):
        self.width = new_width
    def self_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        diagonal = ((self.width ** 2) + (self.height ** 2)) ** 0.5
        return diagonal 
    
    def git_picture(self):
        if self.height > 50 or self.width > 50:
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
    
    def __str__(self):
        if __class__ == "Rectangle":
            return f"Rectangle(width={self.width}, height={self.height}"