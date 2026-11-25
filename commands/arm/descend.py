from subsystems.arm import Arm
from ultime.command import Command


class Descend(Command):
    def __init__(self, arm: Arm):
        super().__init__()
        self._arm = arm
        self.addRequirements(self._arm)

    def initialize(self):
        pass

    def execute(self):
        self._arm.move_down_arm()

    def isFinished(self) -> bool:
        return self._arm.is_down()

    def end(self, interrupted: bool) -> None:
        self._arm.maintain_arm()
