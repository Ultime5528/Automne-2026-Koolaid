from subsystems.grabber import Grabber
from ultime.command import Command


class Ungrab(Command):
    def __init__(self, grabber: Grabber):
        super().__init__()
        self._grabber = grabber
        self.addRequirements(self._grabber)

    def execute(self):

        self._grabber.ungrab_cylinder()

    def isFinished(self) -> bool:
        return not self._grabber.have_grabbed()

    def end(self, interrupted: bool) -> None:
        self._grabber.stop()
