from ultime.immutable import Immutable

"""
Respect the naming convention : "subsystem" _ "component type" _ "precision"

Put port variables into the right category: CAN - PWM - DIO

Order port numbers, ex:
    shooter_motor = 0
    drivetrain_motor_fr = 1
    drivetrain_motor_rr = 2
"""


class CAN(Immutable):
    arm_motor = 1
    slide_motor = 2


class PWM(Immutable):
    grabber_motor = 1
    funnel_servo = 2


class DIO(Immutable):
    arm_switch_up = 1
    arm_switch_down = 2
    grab_switch = 3


class PDP(Immutable):
    pass
