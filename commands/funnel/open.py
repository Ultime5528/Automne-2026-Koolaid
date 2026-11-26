from ultime.command import Command
from subsystems.funnel import Funnel


class Open(Command):
    def __init__(self, funnel: Funnel):
        super().__init__()
        self._funnel = funnel
        self.addRequirements(self._funnel)

    def initialize(self):
        pass

    def execute(self):
        self._funnel.open()

    def end(self, interrupted: bool):
        pass
