# s24005
# 実行が確認出来たら時間を表示させる「時計アプリ」を作ってみたい
# 時計アプリをモジュール名「time_kadai.py」で作成します
# 時計アプリを使いやすくバージョンアップしていきます

import datetime
import tkinter as tk # GUIでアプリを作ることができるモジュール

# 時間を処理する部分を実装
def update_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%Y年%m月%d日 %H時%M分%S秒")
    #
    lbl.config(text=current_time)
    root.after(1000, update_time)

# Tkinterのウインドウを作成
root = tk.Tk() # 初めのおまじない

root.title("時計アプリ")
# デザイン
lbl = tk.Label()
lbl.config(text="", font=("Helvetica", 20))
lbl.pack()

# 関数の呼び出し
update_time()

root.mainloop() # 終わりのおまじない
