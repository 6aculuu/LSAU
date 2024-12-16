#!/usr/bin/env python3
import math
import time
import csv
from ev3dev.ev3 import LargeMotor
from ev3dev2.power import PowerSupply

# Initialize motor and power supply
motorA = LargeMotor('outA')
power = PowerSupply()
max_volts = power.measured_volts  # Measure battery voltage once
print("Volts: " + str(max_volts))

# Function to write data to CSV file
def log_to_csv(filename, data):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # writer.writerow(["Time (s)", "Signal (V)", "Angle (degrees)", "Angular speed (deg/s)"])
        writer.writerows(data)

# Function to convert amplitude to duty cycle percentage
def volts_to_duty_cycle(volts, max_volts):
    return (volts / max_volts) * 100

# Function to apply A1*sin(w1*t)
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

# Function to apply A2*cos(w2*t) + A3*sin(w3*t)
def apply_combined_wave(motor, A2_volts, w2, A3_volts, w3, duration, filename):
    A2 = volts_to_duty_cycle(A2_volts, max_volts)
    A3 = volts_to_duty_cycle(A3_volts, max_volts)
    start_time = time.time()
    data = []
    while (time.time() - start_time) < duration:
        t = time.time() - start_time
        duty_cycle = A2 * math.cos(w2 * t) + A3 * math.sin(w3 * t)
        motor.run_direct(duty_cycle_sp=int(duty_cycle))
        data.append([
            t,
            duty_cycle / 100 * max_volts,
            motor.position,
            motor.speed
        ])
    motor.run_direct(duty_cycle_sp=0)
    log_to_csv(filename, data)

# Main code
try:
    # Example parameters
    A1_volts = 7.2  # Amplitude 7.2 V
    w1 = 2 * math.pi * 0.5  # Frequency 0.5 Hz
    A2_volts = 3.0  # Amplitude 5.0 V
    w2 = 2 * math.pi * 0.3  # Frequency 0.3 Hz
    A3_volts = 3.0  # Amplitude 6.0 V
    w3 = 2 * math.pi * 0.7  # Frequency 0.7 Hz

    sim_time = 5

    # Choose wave type
    choice = input("Select wave type (1 - A1*sin(w1*t), 2 - A2*cos(w2*t) + A3*sin(w3*t)): ")

    # Get timestamp for file name
    timestamp = time.strftime("%Y%m%d_%H%M%S")

    if choice == '1':
        print("Applying A1*sin(w1*t)")
        apply_sine_wave(motorA, A1_volts, w1, duration=sim_time, filename='task5_1_{}.csv'.format(timestamp))
    elif choice == '2':
        print("Applying A2*cos(w2*t) + A3*sin(w3*t)")
        apply_combined_wave(motorA, A2_volts, w2, A3_volts, w3, duration=sim_time, filename='task5_2_{}.csv'.format(timestamp))
    else:
        print("Invalid choice")

except Exception as e:
    print("Error: {}".format(e))
finally:
    motorA.stop(stop_action='brake')
