#!/usr/bin/env python3
import math
import time
import csv
from ev3dev.ev3 import LargeMotor
from ev3dev2.power import PowerSupply

# Инициализация мотора и питания
motorA = LargeMotor('outA')
power = PowerSupply()
max_volts = power.measured_volts  # Измеряем напряжение батареи один раз
print("Volts: " + str(max_volts))