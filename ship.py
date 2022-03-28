from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Ship(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.penup()
        self.go_to_start()
        self.setheading(90)
#move in all four direction
    def go_up(self):
        self.fd(MOVE_DISTANCE)
    def go_down(self):
        self.bk(MOVE_DISTANCE)
    def go_right(self):
        self.rt(MOVE_DISTANCE)
    def go_left(self):
        self.lt(MOVE_DISTANCE)


    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def get_position(self):
        sp = self.position

        return sp

    def is_at_finsih_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False






