# GUIで動くアプリを作ってみるよ

import tkinter as tk #まずこの行を書く必要があるよ

root = tk.Tk() #初めのおまじない

root.geometry("300x200") # ウィンドウのサイズを決める
root.title("ハローアプリ") # ウィンドウのタイトルを決める
lbl = tk.Label(text="Hello World") # いつもの
lbl.pack() # lblを配置させる必要があるよ

root.mainloop() # 終わりのおまじない
