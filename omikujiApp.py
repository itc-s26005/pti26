import tkinter as tk
import random

def dispLabel():
    kuji = ["大吉", "中吉", "小吉", "凶"] #おみくじのリストを用意
    lbl.configure(text=random.choice(kuji)) #ランダムに一つ選んで用意

root = tk.Tk() #ここから先はこれまでのプログラムと一緒
root.geometry("500x300")

lbl = tk.Label(text="LABEL")
btn = tk.Button(text="PUSH",command = dispLabel)

lbl.pack()
btn.pack()
tk.mainloop()


