# s24005 def4_kadai.py
# main()関数を使っておみくじの結果をランダムで表示します
#

import random
def omikuji():
    kuji = ["大吉","中吉","小吉","凶"]
    return random.choice(kuji)

def main():
    kekka = omikuji()
    print("結果は", kekka, "です")

if __name__ == "__main__":
    main()
