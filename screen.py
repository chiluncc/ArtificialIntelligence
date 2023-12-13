import tkinter as tk
from PIL import ImageGrab
import win32gui
import win32con
import os

def take_screenshot(hwnd, title):
    rect = win32gui.GetWindowRect(hwnd)
    x, y, right, bottom = rect
    w = right - x
    h = bottom - y
    if w > 0 and h > 0:
        screenshot = ImageGrab.grab((x, y, right, bottom))
        screenshot.save(f"{title}.png")
        print(f"Screenshot of {title} saved!")
    else:
        print(f"Skipping {title} - Invalid coordinates.")

def get_windows():
    def handle_window(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd):
            windows[hwnd] = win32gui.GetWindowText(hwnd)

    windows = {}
    win32gui.EnumWindows(handle_window, windows)
    return windows

def display_windows():
    windows = get_windows()

    def on_click(hwnd):
        def inner():
            title = windows[hwnd]
            take_screenshot(hwnd, title)
        return inner

    root = tk.Tk()
    root.title("Window Screenshots")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    for hwnd, title in windows.items():
        button = tk.Button(frame, text=title, command=on_click(hwnd))
        button.pack(fill=tk.X)

    root.mainloop()

if __name__ == "__main__":
    display_windows()
