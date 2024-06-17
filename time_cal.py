# time_cal.py
# 現在の時刻と2024年6月のカレンダーを表示する
#
def time_cal():
    import datetime
    n = datetime.datetime.now()
    d = n.strftime("%Y年%m月%d日 %H:%M:%S")
    import calendar as cal
    c = cal.month(2024,6)
    print(d)
    print(c)
    return
