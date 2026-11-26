from ultime.command import Command
from subsystems.funnel import Funnel


class Close(Command):
    def __init__(self, funnel: Funnel):
        super().__init__()
        self._funnel = funnel
        self.addRequirements(self._funnel)

    def initialize(self):
        pass

    def execute(self):
        self._funnel.close()

    def end(self, interrupted: bool):
        pass
