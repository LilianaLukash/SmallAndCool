import pyautogui
from PIL import ImageGrab
import pytesseract
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename
from models import *

# Функція для отримання скріншоту та збереження його у файл
def capture_screenshot():
    screenshot = pyautogui.screenshot()
    return screenshot

# Функція для виділення частини скріншоту
def select_area(image):
    # Тут може бути код для виділення області
    # Наприклад, використовуючи Tkinter
   
def capture_area():
    app = ScreenCaptureTool()
    app.mainloop()
    return app.selected_area

selected_area = capture_area()
print("Вибрана область:", selected_area)

# Функція для конвертації зображення в текст
def image_to_text(image):
    text = pytesseract.image_to_string(image)
    return text

# Запуск програми
def main():
    screenshot = capture_screenshot()
    selected_area = select_area(screenshot)
    text = image_to_text(selected_area)

    # Збереження тексту у файл
    filename = asksaveasfilename(defaultextension=".txt")
    with open(filename, 'w') as file:
        file.write(text)

    print("Текст успішно збережено у файлі:", filename)

if __name__ == "__main__":
    main()
