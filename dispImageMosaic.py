import tkinter as tk #ウインドウを表示する
import tkinter.filedialog as fd #ファイルダイアログを使うモジュール
import PIL.Image #画像を扱うモジュール
import PIL.ImageTk #tkinterで作った画面上に画像を表示させるモジュール

def dispPhoto(path):
    #画像を読み込んで、グレースケールに変換する
    newImage = PIL.Image.open(path).convert("L").resize((32,32)).resize((300,300), resample=0)
    #そのイメージラベルを表示する
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData

def openFile(): #ファイルログを開くための関数
    fpath = fd.askopenfilename() #ファイルダイアログを開いて、選択したファイル名を取得する

    if fpath: #もしファイル名が合ったら
        dispPhoto(fpath) #そのファイル名を関数で呼び出す

root = tk.Tk()          #画面を作る
root.geometry("400x350")

btn = tk.Button(text="ファイルを開く", command = openFile) #ボタンを作って関数を設定する
imageLabel = tk.Label() #画面に表示用のラベルを作る
btn.pack() #画面にボタンを設置する
imageLabel.pack() #画面にラベルを配置する
tk.mainloop() #作ったウィンドウを表示する
