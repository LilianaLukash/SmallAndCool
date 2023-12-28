class ScreenCaptureTool(tk.Tk):
    def __init__(self):
        super().__init__()
        self.start_x = None
        self.start_y = None
        self.rect = None
        self.deiconify()
        self.attributes("-fullscreen", True)
        self.canvas = tk.Canvas(self, cursor="cross", bg="grey", opacity=0.3)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
        self.selected_area = None

    def on_button_press(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        if not self.rect:
            self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, 1, 1, outline="red")

    def on_move_press(self, event):
        cur_x = self.canvas.canvasx(event.x)
        cur_y = self.canvas.canvasy(event.y)
        self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

    def on_button_release(self, event):
        self.selected_area = (self.start_x, self.start_y, self.canvas.canvasx(event.x), self.canvas.canvasy(event.y))
        self.capture_selected_area()
        self.destroy()

    def capture_selected_area(self):
        x1, y1, x2, y2 = self.selected_area
        image = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        # Тут можна виконати додаткові дії з захопленим зображенням