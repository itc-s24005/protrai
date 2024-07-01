# s24005
#

import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image, PIL.ImageTk

def dispPhoto(path):
    newImage = PIL.Image.open(path).resize((300,300))
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData
    lbl2 = tk.Label(text=path, font=("Helvetica", 16))
    lbl2.pack()

def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        dispPhoto(fpath)
        print(fpath)

root = tk.Tk()
root.geometry("500x450")

Static1 = tk.Label(text=u'画像表示アプリ　バージョン2.0')
btn = tk.Button(text="ファイルを開く", command = openFile)
imageLabel = tk.Label()
Static1.pack()
btn.pack()
imageLabel.pack()

tk.mainloop()
