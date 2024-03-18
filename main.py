import threading
import tkinter as tk
from PIL import ImageGrab
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'
import keyboard
from time import sleep
import threading
from openai import OpenAI
from tkinter import messagebox

class CaptureScreen:
    def __init__(self, root, scale):
        self.root = root
        self.begin_x = None
        self.begin_y = None
        self.end_x = None
        self.end_y = None
        self.scale = scale

        self.selection = None
        self.start_point = None
        self.rect = None

        root.attributes('-fullscreen', True)
        root.attributes('-alpha', 0.3)  # Прозорість

        self.canvas = tk.Canvas(root, cursor="cross")
        self.canvas.pack(fill="both", expand=True)

        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

    def on_button_press(self, event):
        self.start_point = event
        self.begin_x = int(event.x )
        self.begin_y = int(event.y )

        if not self.rect:
            self.rect = self.canvas.create_rectangle(self.begin_x, self.begin_y, self.begin_x, self.begin_y, outline='red')

    def on_move_press(self, event):
        curX, curY = int(event.x ), int(event.y )

        if self.rect:
            self.canvas.coords(self.rect, self.begin_x, self.begin_y, curX, curY)

    def on_button_release(self, event):
        print("Відпускання кнопки")
        self.end_x = int(event.x )
        self.end_y = int(event.y )
        self.root.quit()

def image_to_text(image):
    text = pytesseract.image_to_string(image)
    return text

def capture_area():
    print("capture_area")
    global screenshot
    scale = 1.5  # Default scale
    root = tk.Tk()
    root.focus_force()
    capture_screen = CaptureScreen(root, scale)
    root.mainloop()

    # Calculate coordinates based on the screen scale
    x1, y1, x2, y2 = capture_screen.begin_x * scale, capture_screen.begin_y * scale, capture_screen.end_x * scale, capture_screen.end_y * scale

    # Capture the screen area
    screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    #screenshot.show()

    # Process the screenshot
    if screenshot:
        text = image_to_text(screenshot)
        text_clean = "розпізнай запитання та дай на нього коротку відповідь мовою запитання. якщо є варіанти відповідей почни з вказування правильного варіанту."
        text_clean = text_clean + " ".join(text.split())
        print(text_clean)
        client = OpenAI()
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
        {"role": "system", "content": "You are a teacher who are helping to make homework."},
        {"role": "user", "content": text_clean}
        ] )

        print(completion.choices[0].message)
        root = tk.Tk()
        root.withdraw()  # Це запобігає відображенню порожнього вікна Tkinter
        tk.messagebox.showinfo("Відповідь", completion.choices[0].message)  
             
        root.destroy()

        return completion.choices[0].message

def on_hotkey_press():
    print("on_hotkey_press")
    thread = threading.Thread(target=capture_area)
    thread.start()
    thread.join()

# capture_area()

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

if __name__ == "__main__":
    main()