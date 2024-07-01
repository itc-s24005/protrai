# app2.py バージョン２

import tkinter as tk # tkinterをimportしてtkとして略す

def dispLabel():
    lbl.config(text="こんにちは")

root = tk.Tk()# 画面を作る
root.geometry("400x200") # 画面の大きさを決める

# ラベルを作る
lbl = tk.Label(text="LABEL", font=("Helvetica", 20))
btn = tk.Button(text="PUSH", command=dispLabel, font=("Helvetica", 20))# ボタンを作る

lbl.pack() # 画面にラベルを配置する
btn.pack() # 画面にボタンを配置する
lbl2 = tk.Label(text="ラベル２", font=("Helbetica", 20)).pack()
btn2 = tk.Button(text="何もしないボタン", command=dispLabel, font=("helberica", 20)).pack
tk.mainloop # 作ったウインドウを表示する
