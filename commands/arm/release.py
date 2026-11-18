from subsystems.arm import Arm
from ultime.command import Command


class Release(Command):
    def __init__(self, arm: Arm):
        super().__init__()
        self._arm = arm
        self.addRequirements(self._arm)

    def initialize(self):
        pass

    def execute(self):
        self._arm.stop()

    def isFinished(self) -> bool:
        return False

    def end(self, interrupted: bool) -> None:
        pass
