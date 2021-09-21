from app_modules import *
import numpy as np
import math as m
import time
from Libs.Magician_Robotics_Libs import *
class Userfunctions(MainWindow):
    def initialize_robot(self):
        self.Robot = Magician()
