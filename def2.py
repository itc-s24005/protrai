# s24005 def2.py
# 関数で消費税を計算するコード
#

def postTaxprice(price):
    ans = price * 1.1
    return ans

print(postTaxprice(120),"円")
print(postTaxprice(128),"円")
print(postTaxprice(980),"円")
