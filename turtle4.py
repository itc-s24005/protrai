# turtle1.py
# 幾何学模様を描きます。

from turtle import * #タートルグラフィックスを使う準備
shape("turtle") #カメの登場
col = ["black","gray"] * 18
for i in range(14):
    color(col[i])
    circle(100) # 半径100の円を描くこと
    left(25) 

done() # おしまい
