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
        self.arm_state = ArmState.off
        self._motor = rev.SparkFlex(
            ports.CAN.arm_motor, rev.SparkFlex.MotorType.kBrushless
        )
        self.switch_up = Switch(Switch.Type.NormallyOpen, ports.DIO.arm_switch_up)
        self.switch_down = Switch(Switch.Type.NormallyOpen, ports.DIO.arm_switch_down)

    def move_up_arm(self):
        self._motor.set(self.speed_up)

    def logValues(self):
        super().logValues()
        self.log("arm_state", str(self.arm_state))

    def move_down_arm(self):
        self._motor.set(self.speed_down)

    def maintain_arm(self):
        self._motor.set(self.speed_maintain)

    def stop(self):
        self._motor.stopMotor()
