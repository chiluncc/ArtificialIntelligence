import tkinter as tk
from tkinter import filedialog

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        print("选择的文件是：", file_path)

root = tk.Tk()
root.title("文件选择器")

select_button = tk.Button(root, text="选择文件", command=select_file)
select_button.pack()

root.mainloop()