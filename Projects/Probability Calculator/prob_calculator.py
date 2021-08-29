import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.colors_quantity = kwargs
        self.contents = list()
        for key,value  in self.colors_quantity.items():
            for i in range(0, value):
                self.contents.append(key)
    
    def draw(self, number_of_draws):
        balls_drawed = []
        if number_of_draws > len(self.contents):
            return self.contents
        '''The following code will draw a ball a "number_of_draws" times
        getting the current size of the list of balls, getting a random 
        index to remove a ball from the list, saving the color name of the ball,
        adding it to the balls_drawed, removing it from the contents list - 
        -where the ball were, and then going to the next draw'''
        while number_of_draws > 0: 
            range_draw = len(self.contents) 
            index_draw = random.randrange(0, range_draw)
            color_ball = self.contents[index_draw]
            balls_drawed.append(self.contents[index_draw])
            self.contents.remove(color_ball)
            number_of_draws -= 1
        return balls_drawed





