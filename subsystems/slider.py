import rev
import wpilib

import ports
from ultime.subsystem import Subsystem
from ultime.autoproperty import autoproperty

from ultime.subsystem import Subsystem
from ultime.switch import Switch


class Slider(Subsystem):
    speed_left = autoproperty(10.5)
    speed_right = autoproperty(10.0)
    def __init__(self):
        super().__init__()
        self._motor = rev.SparkFlex(
             ports.CAN.slide_motor, rev.SparkFlex.MotorType.kBrushless
             )
        self.switch_up = Switch(Switch.Type.NormallyOpen, ports.DIO.arm_switch_up)
        self.switch_down = Switch(Switch.Type.NormallyOpen, ports.DIO.arm_switch_down)



    def slide_left(self):
        self._motor.set(self.speed_left)


    def slide_right(self):
        self._motor.set(self.speed_right)

    def stop(self):
        self._motor.stopMotor()

