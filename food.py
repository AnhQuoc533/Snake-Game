from snake import *
import random


class SnakeFood(turtle.Turtle):

    def __init__(self, snake_body: list):
        self.food_icons = []
        self.__add_icons()

        super().__init__()
        self.shape(random.choice(self.food_icons))
        self.penup()
        self.shapesize()
        self.speed("fastest")
        self.refresh(snake_body)

    def __add_icons(self):
        import os

        icons = os.listdir('gfx')
        for icon in icons:
            if icon != 'border.gif':
                food_icon = 'gfx/' + icon
                turtle.addshape(food_icon)
                self.food_icons.append(food_icon)

    def refresh(self, snake_body: list):
        while True:
            x = random.randint(-14, 14) * TURTLE_SIZE
            y = random.randint(-14, 14) * TURTLE_SIZE

            # Avoid putting food at the position of snake's body
            is_conflict = False
            for fragment in snake_body:
                if fragment.distance(x, y) < 10:
                    is_conflict = True
                    break

            if not is_conflict:
                self.shape(random.choice(self.food_icons))
                self.goto(x, y)
                break
