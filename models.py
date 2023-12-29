import tkinter as tk
from PIL import ImageGrab

class CaptureScreen:
    def __init__(self, root):
        self.root = root
        self.begin_x = None
        self.begin_y = None
        self.end_x = None
        self.end_y = None

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
        self.begin_x = event.x
        self.begin_y = event.y

        if not self.rect:
            self.rect = self.canvas.create_rectangle(self.begin_x, self.begin_y, self.begin_x, self.begin_y, outline='red')

    def on_move_press(self, event):
        curX, curY = (event.x, event.y)

        if self.rect:
            self.canvas.coords(self.rect, self.begin_x, self.begin_y, curX, curY)



    def on_button_release(self, event):
        print("Відпускання кнопки")
        self.end_x, self.end_y = (event.x, event.y)
        self.root.quit()

def capture_area():
    root = tk.Tk()
    capture_screen = CaptureScreen(root)
    root.mainloop()

    # Координати виділеної області
    x1, y1, x2, y2 = capture_screen.begin_x, capture_screen.begin_y, capture_screen.end_x, capture_screen.end_y

    # Захоплення скріншоту обраної області
    screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    return screenshot

# Приклад використання
#screenshot = capture_area()

#screenshot.show()
