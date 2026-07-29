from turtle import Turtle,Screen
MOVE_DISTANCE = 20
STARTING_POSITON = []
class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for i in range(3):
            x = i * 20
            positon = (-x, 0)
            self.add_seg(positon)


    def add_seg(self, positon):
        seg = Turtle()
        seg.color("white")
        seg.shape("square")
        seg.penup()
        seg.setposition(positon)
        self.snake_body.append(seg)

    def extend(self):
        self.add_seg(self.snake_body[-1].position())

    def move(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            x = self.snake_body[i - 1].xcor()
            y = self.snake_body[i - 1].ycor()
            self.snake_body[i].goto(x, y)

        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_body[0].heading() != 270:
            self.snake_body[0].setheading(90)

    def down(self):
        if self.snake_body[0].heading() != 90:
            self.snake_body[0].setheading(270)

    def right(self):
        if self.snake_body[0].heading() != 180:
            self.snake_body[0].setheading(0)

    def left(self):
        if self.snake_body[0].heading() != 0:
            self.snake_body[0].setheading(180)

    def reset(self):
        for seg in self.snake_body:
            seg.goto(1000,1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]