import SimpleModel
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

names = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "方块", "黑桃", "红桃", "梅花"]
nums = [i for i in range(17)]
nums2names = dict(zip(nums, names))

model = SimpleModel.SimpleModel(400, 200, 100, 17, numX = 20, numY = 20)
model.loadModel("Z_TEMP")

root = tk.Tk()
root.title("选择图片")

frame = tk.Frame(root, padx = 70)
frame.pack()

imgLabel = tk.Label(frame, padx = 40, pady = 20)
imgLabel.pack()

txtLabel = tk.Label(frame, padx = 40, pady = 5)
txtLabel.pack()

def whilePress(model = model):
    filename = filedialog.askopenfilename()
    img = Image.open(filename)
    img_tk = ImageTk.PhotoImage(img)
    imgLabel.config(image = img_tk)
    imgLabel.image = img_tk

    tempList= model.readImageOnly(filename)
    outputs, index = model.use(tempList)
    txtLabel.config(text = f"最终判断：{nums2names[int(index)]}")
    

button = tk.Button(frame, command = whilePress, text = "更换图片")
button.pack()

root.mainloop()