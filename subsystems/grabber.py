import rev
import wpilib

import ports
from ultime.subsystem import Subsystem
from ultime.autoproperty import autoproperty

from ultime.subsystem import Subsystem
from ultime.switch import Switch


class Grabber(Subsystem):
    speed_grab = autoproperty(10.5)
    speed_ungrab = autoproperty(10.0)
    speed_maintain = autoproperty(0.06)

    def __init__(self):
        super().__init__()

        self._motor = self._motor = rev.SparkMax(
            ports.CAN.slide_motor, rev.SparkMax.MotorType.kBrushless
        )
        self.switch = Switch(Switch.Type.NormallyOpen, ports.DIO.grab_switch)

    def grab_cylinder(self):
        self._motor.set(self.speed_grab)

    def ungrab_cylinder(self):
        self._motor.set(self.speed_ungrab)

    def maintain_cylinder(self):
        self._motor.set(self.speed_maintain)

    def stop(self):
        self._motor.stopMotor()
