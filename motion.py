#!/usr/bin/python3
import Servo, time

class motion(object):
    """
        Class to control the motion of the rover.
        Attributes:
            offset: An adjustment to straighten the steering when centered at 90 degrees

        TODO:
            Implement forward function
            Implement reverse funciton
            Implement left steer
            Implement right steer
            Implement stop
            Implement offset
    """

    def __init__(self):
        self.offset = 0
        self.servo = Servo.Servo(0)
        self.servo.setup()

    def forward(self, speed):
        """Move Rover forward.

        Args:
            speed (int): the speed we want to go forward (0-100).
        """
        print("Forward")

    def reverse(self):
        print("Reverse")

    def stop(self):
        print("Stop")

    def left(self):
        print("Left")

    def right(self):
        print("Right")

    def center(self):
        print("Center")
        for i in range(90, 170, 5):
            print(i)
            self.servo.write(i)
            time.sleep(0.1)
        for i in range(170, 10, -5):
            print(i)
            self.servo.write(i)
            time.sleep(0.1)
        for i in range(10, 90, 5):
             print(i)
             self.servo.write(i)
             time.sleep(0.1)

if __name__ == '__main__':
    move = motion()
    move.center()