from subsystems.grabber import Grabber
from ultime.command import Command


class Grab(Command):
    def __init__(self, grabber: Grabber):
        super().__init__()
        self._grabber = grabber
        self.addRequirements(self._grabber)

    def execute(self):

        self._grabber.grab_cylinder()

    def isFinished(self) -> bool:
        return self._grabber.have_grabbed()

    def end(self, interrupted: bool) -> None:
        self._grabber.maintain_cylinder()
