#!/usr/bin/env python3
import wpilib

from modules.control import ControlModule
from modules.dashboard import DashboardModule
from modules.hardware import HardwareModule
from modules.logging import LoggingModule
from modules.propertysavechecker import PropertySaveCheckerModule
from ultime.modulerobot import ModuleRobot


class Robot(ModuleRobot):
    # robotInit fonctionne mieux avec les tests que __init__
    def __init__(self):
        super().__init__()

        wpilib.LiveWindow.disableAllTelemetry()
        wpilib.DriverStation.silenceJoystickConnectionWarning(True)
        # self.enableLiveWindowInTest(False)

        self.hardware = self.addModule(HardwareModule())





        self.control = self.addModule(ControlModule(self.hardware))

        self.dashboard = self.addModule(
            DashboardModule(
                self.hardware, self.modules
            )
        )
        self.logging = self.addModule(LoggingModule())
        self.property_save_checker = self.addModule(PropertySaveCheckerModule())

