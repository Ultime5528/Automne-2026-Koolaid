import modulefinder

import commands2
import wpilib
from commands2 import CommandScheduler
from pathplannerlib.path import PathPlannerPath
from wpilib import SmartDashboard
from wpimath.geometry import Pose2d



from commands.grabber.grab import Grab
from commands.grabber.ungrab import Ungrab
from commands.arm.arise import Arise
from commands.arm.descend import Descend
from commands.arm.release import Release
from commands.guide import ManualMoveGuide, ResetGuide, MoveGuide
from modules.hardware import HardwareModule
from subsystems.arm import Arm

from ultime.log import Logger
from ultime.module import Module, ModuleList


class DashboardModule(Module):
    def __init__(
        self,
        hardware: HardwareModule,

        module_list: ModuleList,
    ):
        super().__init__()
        self._hardware = hardware
        self._module_list = module_list
        self.setupCopilotCommands(hardware)
        self.setupCommands(hardware)


    def setupCopilotCommands(self, hardware: HardwareModule):
        pass

    def setupCommands(self, hardware):
        """
        Drivetrain
        """
        # putCommandOnDashboard("Drivetrain", ResetGyro(hardware.drivetrain, ))

        """
        Arm
        """
        putCommandOnDashboard("Arm", Arise(hardware.arm))
        putCommandOnDashboard("Arm", Descend(hardware.arm))
        putCommandOnDashboard("Arm", Release(hardware.arm))
        """
        Grabber
        """
        putCommandOnDashboard("Grabber", Grab(hardware.grabber))
        putCommandOnDashboard("Grabber", Ungrab(hardware.grabber))


        """
        Hugger
        """

        """
        Feeder
        """


        """
        Pivot
        """


        """
        Group
        """


    def robotInit(self) -> None:
        for subsystem in self._hardware.subsystems:
            Logger.getInstance().addLoggable(subsystem)

        for module in self._module_list.modules:
            Logger.getInstance().addLoggable(module)


        wpilib.SmartDashboard.putData(
            "CommandScheduler", CommandScheduler.getInstance()
        )
        wpilib.SmartDashboard.putData("PDP", self._hardware.pdp)

        for module in self._module_list.modules:
            if module.redefines_init_sendable:
                """
                If a module keeps a reference to a subsystem or the HardwareModule,
                it should be wrapped in a weakref.proxy(). For example,
                self.hardware = proxy(hardware)
                """
                print("Putting on dashboard:", module.getName())
                wpilib.SmartDashboard.putData(module.getName(), module)


def putCommandOnDashboard(
    sub_table: str, cmd: commands2.Command, name: str = None, suffix: str = " commands"
) -> commands2.Command:
    if not isinstance(sub_table, str):
        raise ValueError(
            f"sub_table should be a str: '{sub_table}' of type '{type(sub_table)}'"
        )

    if suffix:
        sub_table += suffix

    sub_table += "/"

    if name is None:
        name = cmd.getName()
    else:
        cmd.setName(name)

    wpilib.SmartDashboard.putData(sub_table + name, cmd)

    return cmd
