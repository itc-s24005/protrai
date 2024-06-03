# s24005
#これはボタンを押すとおみくじの結果を表示します

import tkinter as tk

def calc():
    import omikuji as tk
root = tk.Tk()

root.geometry("300x200")
root.title("おみくじ")
lbl = tk.Label(text="おみくじです")
lbl.pack()
calcButton = tk.Button(text="結果を見る")
calcButton["command"] = calc
calcButton.pack()
root.mainloop
