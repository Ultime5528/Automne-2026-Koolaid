import rev
import wpilib

import ports
from ultime.subsystem import Subsystem
from ultime.autoproperty import autoproperty

from ultime.subsystem import Subsystem
from ultime.switch import Switch


class Arm(Subsystem):
    speed_down = autoproperty(10.5)
    speed_up = autoproperty(10.0)
    speed_maintain = autoproperty(0.06)

    def __init__(self):
        super().__init__()

        self._motor = rev.SparkFlex(
            ports.CAN.arm_motor, rev.SparkFlex.MotorType.kBrushless
        )
        self._switch_up = Switch(Switch.Type.NormallyOpen, ports.DIO.arm_switch_up)
        self._switch_down = Switch(Switch.Type.NormallyOpen, ports.DIO.arm_switch_down)

    def move_up_arm(self):
        self._motor.set(self.speed_up)

    def logValues(self):
        super().logValues()
        self.log("is_up", self.is_up())
        self.log("is_down", self.is_down())

    def is_up(self) -> bool:
        return self._switch_up.isPressed()

    def is_down(self) -> bool:
        return self._switch_down.isPressed()

    def move_down_arm(self):
        self._motor.set(self.speed_down)

    def maintain_arm(self):
        self._motor.set(self.speed_maintain)

    def stop(self):
        self._motor.stopMotor()
