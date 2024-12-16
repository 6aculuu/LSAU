#!/usr/bin/env python3
import math
import time
import csv
from ev3dev.ev3 import LargeMotor
from ev3dev2.power import PowerSupply

motorA = LargeMotor('outA')
power = PowerSupply()
max_volts = power.measured_volts 
print("Volts: " + str(max_volts))

def log_to_csv(filename, data):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def volts_to_duty_cycle(volts, max_volts):
    return (volts / max_volts) * 100

def apply_sine_wave(motor, A1_volts, w1, duration, filename):
    A1 = volts_to_duty_cycle(A1_volts, max_volts)
    start_time = time.time()
    data = []
    while (time.time() - start_time) < duration:
        t = time.time() - start_time
        duty_cycle = A1 * math.sin(w1 * t)
        motor.run_direct(duty_cycle_sp=int(duty_cycle))
        data.append([
            t,
            duty_cycle / 100 * max_volts,
            motor.position,
            motor.speed
        ])
    motor.run_direct(duty_cycle_sp=0)
    log_to_csv(filename, data)

try:
    frequencies = [0.3, 1, 5, 10, 20]  
    amplitudes = [5.0, 5.0, 5.0, 5.0, 5.0]  

    sim_time = 5

    timestamp = time.strftime("%Y%m%d_%H%M%S")

    for i, freq in enumerate(frequencies):
        A_volts = amplitudes[i]
        w = 2 * math.pi * freq
        apply_sine_wave(motorA, A_volts, w, duration=sim_time, filename='sine_wave_{}Hz_{}.csv'.format(freq, timestamp))
        time.sleep(2)

except Exception as e:
    print("error")
finally:
    motorA.stop(stop_action='brake')
