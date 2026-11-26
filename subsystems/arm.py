import rev
import wpilib

import ports
from ultime.subsystem import Subsystem
from ultime.autoproperty import autoproperty

from ultime.subsystem import Subsystem
from ultime.switch import Switch


class Arm(Subsystem):
    speed_left = autoproperty(10.5)
    speed_right = autoproperty(10.0)
    speed_maintain = autoproperty(0.06)

    def __init__(self):
        super().__init__()
        self._motor = rev.SparkFlex(
            ports.CAN.arm_motor, rev.SparkFlex.MotorType.kBrushless
        )
        self.switch_up = Switch(Switch.Type.NormallyOpen, ports.DIO.arm_switch_up)
        self.switch_down = Switch(Switch.Type.NormallyOpen, ports.DIO.arm_switch_down)

    def rise(self):
        self._motor.set(self.speed_right)

    def descend(self):
        self._motor.set(self.speed_left)

    def maintain_arm(self):
        self._motor.set(self.speed_maintain)

    def stop(self):
        self._motor.stopMotor()
