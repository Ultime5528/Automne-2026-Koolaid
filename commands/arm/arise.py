from subsystems.arm import Arm
from ultime.command import Command


class Arise(Command):
    def __init__(self, arm: Arm):
        super().__init__()
        self._arm = arm
        self.addRequirements(self._arm)

    def initialize(self):
        pass
    def execute(self):
        self._arm.rise()


    def isFinished(self) -> bool:
        return  self._arm.switch_up.isPressed()


    def end(self, interrupted: bool) -> None:
        self._arm.maintain_arm()
