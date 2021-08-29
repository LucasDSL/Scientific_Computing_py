from prob_calculator import Hat as h 
from prob_calculator import experiment
hat = h(red=3,blue=2)
"print(hat.draw(7))"

hat = h(black=6, red=4, green=3)
probability = experiment(hat=hat, 
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)