import pyautogui
from PIL import ImageGrab
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename
from models import *
import pytesseract
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'


# Функція для конвертації зображення в текст
def image_to_text(image):
    text = pytesseract.image_to_string(image)
    return text

# Запуск програми
def main():
    screenshot = capture_area()
    text = image_to_text(screenshot)
    print(text)

    # Збереження тексту у файл
   # filename = asksaveasfilename(defaultextension=".txt")
   # with open(filename, 'w') as file:
   #     file.write(text)

    #print("Текст успішно збережено у файлі:", filename)

if __name__ == "__main__":
    main()
