import tkinter as tk
from tkinter import messagebox
import time
import cricinfo

Score = cricinfo.cricinfo_parser()


root = tk.Tk()
root.title("Cricket Score")

lable = tk.Label(text="Below are the scores")
lable.pack()
lable2 = tk.Label(text=Score)
lable2.pack()
root.geometry("400x100")

root.after(5000,lambda:root.destroy())
root.mainloop()