import pyautogui
import time
import threading
import tkinter as tk

class MouseMover:
    def __init__(self):
        self.is_running = False
        self.thread = None

        self.window = tk.Tk()
        self.window.title("Mouse Mover")

        self.start_button = tk.Button(self.window, text="Start", command=self.start)
        self.start_button.pack()

        self.stop_button = tk.Button(self.window, text="Stop", command=self.stop)
        self.stop_button.pack()

        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.thread = threading.Thread(target=self.move_mouse)
            self.thread.start()

    def stop(self):
        if self.is_running:
            self.is_running = False
            self.thread.join()
            self.thread = None

    def move_mouse(self):
        while self.is_running:
            pyautogui.moveRel(10, 0)  # move mouse cursor 10 pixels to the right
            time.sleep(0.2)  # wait for 0.2 seconds before moving again

    def on_close(self):
        self.stop()
        self.window.destroy()

    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    app = MouseMover()
    app.run()