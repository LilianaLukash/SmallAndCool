import threading
from time import sleep
import pyautogui
from PIL import ImageGrab
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename
from models import *
import pytesseract
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'
import keyboard


# Запуск програми
def main():
    

    while True:
            
        # Перевірка натискання Ctrl+Shift+A
        if keyboard.is_pressed('ctrl+shift+A'):
            on_hotkey_press()
            sleep(0.5)  # Затримка для запобігання миттєвому повторному захопленню

        # Перевірка натискання Esc
        if keyboard.is_pressed('esc'):
            print("Завершення програми.")
            break

    

    # Збереження тексту у файл
   # filename = asksaveasfilename(defaultextension=".txt")
   # with open(filename, 'w') as file:
   #     file.write(text)

    #print("Текст успішно збережено у файлі:", filename)

if __name__ == "__main__":
    main()
