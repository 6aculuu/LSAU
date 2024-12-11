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

# Функция для записи данных в CSV файл
def log_to_csv(filename, data):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # writer.writerow(["Время (с)", "Сигнал (В)", "Угол (градусы)", "Угловая скорость (град/с)"])
        writer.writerows(data)

# Функция для пересчета амплитуды в проценты мощности
def volts_to_duty_cycle(volts, max_volts):
    return (volts / max_volts) * 100

# Функция для задания воздействия A1*sin(w1*t)
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
        # time.sleep(0.01)  # Пауза для плавности управления
    motor.run_direct(duty_cycle_sp=0)
    log_to_csv(filename, data)

# Функция для задания воздействия A2*cos(w2*t) + A3*sin(w3*t)
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
        # time.sleep(0.01)  # Пауза для плавности управления
    motor.run_direct(duty_cycle_sp=0)
    log_to_csv(filename, data)

# Основной код
try:
    # Пример параметров
    A1_volts = 7.2  # Амплитуда 7.2 В
    w1 = 2 * math.pi * 0.5  # Частота 0.5 Гц
    A2_volts = 5.0  # Амплитуда 5.0 В
    w2 = 2 * math.pi * 0.3  # Частота 0.3 Гц
    A3_volts = 6.0  # Амплитуда 6.0 В
    w3 = 2 * math.pi * 0.7  # Частота 0.7 Гц

    sim_time = 5

    # Выбор воздействия
    choice = input("Выберите воздействие (1 - A1*sin(w1*t), 2 - A2*cos(w2*t) + A3*sin(w3*t)): ")

    # Получение временной метки для имени файла
    timestamp = time.strftime("%Y%m%d_%H%M%S")

    if choice == '1':
        print("Применение воздействия A1*sin(w1*t)")
        apply_sine_wave(motorA, A1_volts, w1, duration=sim_time, filename=f'task5_1_{timestamp}.csv')
    elif choice == '2':
        print("Применение воздействия A2*cos(w2*t) + A3*sin(w3*t)")
        apply_combined_wave(motorA, A2_volts, w2, A3_volts, w3, duration=sim_time, filename=f'task5_2_{timestamp}.csv')
    else:
        print("Неверный выбор")

except Exception as e:
    print(f"Ошибка: {e}")
finally:
    motorA.stop(stop_action='brake')
