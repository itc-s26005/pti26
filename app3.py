import tkinter as tk

def dispLabel():   #関数を追加する
    lbl.configure(text="初めてのアプリ") #ラベルの文字を「こんにちは」に変更する

root = tk.Tk() #画面を作る
root.geometry("300x400")

lbl = tk.Label(text="LABEL")
btn = tk.Button(text="PUSH", command = dispLabel) #ボタンで実行できるように修正する

lbl.pack() #画面にラベルを作る
btn.pack() #画面にボタンを配置する
tk.mainloop() #作ったウィンドウを表示する
