# s24005 entry_kadai.py
# エントリーウィジェットで受け付けた金額を税込み（10％）価格として出力するプログラム

import tkinter as tk # tkinterをtkと略して使用する

def dispLabel():
# entryメソッドを使用して入力を受け付け変数aに格納
    a = entry.get()
    # ログの出力
    print(f"aは{type(a)}") # ログの出力
    lbl.config(text=f"{a}さんこんにちは")

root = tk.Tk()
root.title("エントリーウィジェット")
root.geometry("400x200") # 画面の大きさを決める

lbl = tk.Label(text="ラベル", font=("Helvetica", 20))
entry = tk.Entry(font=("Helvetica", 20))
btn = tk.Button(text="ボタン", font=("Helvetica", 20), command=dispLabel)

lbl.pack()
entry.pack()
btn.pack()

tk.mainloop()
