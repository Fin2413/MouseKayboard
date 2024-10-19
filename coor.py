import pyautogui
import time

print("Переместите мышь в нужное место и подождите 2 секунды...")
time.sleep(2)

while True:
    # Получаем текущие координаты курсора
    x, y = pyautogui.position()
    print(f"Координаты: ({x}, {y})", end='\r')  # Перезаписываем строку
