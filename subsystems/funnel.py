import wpilib
from ultime.autoproperty import autoproperty
import ports

from ultime.subsystem import Subsystem


class Funnel(Subsystem):

    angle_close = autoproperty(0.0)
    angle_open = autoproperty(90.0)

    def __init__(self):
        super().__init__()
        self._funnel_servo = wpilib.Servo(ports.PWM.funnel_servo)

    def logValues(self):
        super().logValues()
        self.log("position", self.angle())

    def open(self):
        self._funnel_servo.setAngle(self.angle_open)

    def angle(self):
        return self._funnel_servo.getAngle()

    def close(self):
        self._funnel_servo.setAngle(self.angle_close)
