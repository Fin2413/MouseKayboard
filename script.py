import pyautogui
import time

# Задержка, чтобы было время подготовиться
time.sleep(2)

# Открываем меню "Пуск"
pyautogui.press('win')
time.sleep(1)

# Печатаем "1С: Предприятие"
pyautogui.write('1С', interval=0.1)
time.sleep(1)

# Нажимаем Enter, чтобы запустить программу
pyautogui.press('enter')

# Переходим к координатам кнопки "1С: Предприятие"
x, y = 951, 552  # Замените 100 и 200 на ваши координаты

# Наводим курсор на нужные координаты
pyautogui.moveTo(x, y, duration=0.5)  # Плавное движение к координатам
time.sleep(2)  # Дополнительная задержка

# Нажимаем левую кнопку мыши
pyautogui.click()
time.sleep(3)  # Дополнительная задержка

pyautogui.moveTo(951, 576, duration=0.5)

# Вводим пароль
pyautogui.write('1852', interval=0.1)  # Устанавливаем интервал между нажатиями, если нужно
pyautogui.press('enter')  # Нажимаем Enter для подтверждения

time.sleep(16)  # Дополнительная задержка

pyautogui.moveTo(152, 33, duration=0.5)
pyautogui.click()

time.sleep(0.5)  # Дополнительная задержка

pyautogui.moveTo(188, 56, duration=0.5)
pyautogui.click()

time.sleep(0.5)  # Дополнительная задержка

pyautogui.moveTo(395, 203, duration=0.5)
pyautogui.click()

time.sleep(1)  # Дополнительная задержка

pyautogui.moveTo(21, 199, duration=0.5)
pyautogui.click()

time.sleep(1)  # Дополнительная задержка

pyautogui.moveTo(92, 240, duration=0.5)
pyautogui.doubleClick()