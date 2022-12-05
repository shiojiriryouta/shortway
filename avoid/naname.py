import matplotlib.pyplot as plt
import numpy as np

# 法線を求める関数 ax+bに垂直で点(c,ac+b)を通る法線の関数
def hosen(a,b,c):
    ah = -1/a
    bh = c/a + a*c + b
    return ah,bh

# 船の目的地への直線と被っている陸の範囲を表示する関数
def riku_range(a,b,field):
    s = [-1,-1]
    e = [-1,-1]
    result = []
    for  i in range(21):
        y = a * i + b
        y = int(round(y))
        if y < 0 or y > 20:
            continue
        
        if field[y][i] == 1:
            s = [i,y]
            result.append(s)
            break

    for i in range(s[0],21):
        y = a * i + b
        y = round(y)
        if y < 0 or y > 20:
            continue
        
        if field[y][i] == 0:
            e = [i-1,round(a * (i-1) + b)]
            result.append(e)
            break
    return s,e

#フィールドの定義 陸の範囲 x,y:5～10
field = []
tmp = []
for i in range(21):
    for j in range(21):
        if j >= 5 and j <= 9 and i >= 5 and i <= 9:
            tmp.append(1)
        else:
            tmp.append(0)
    field.append(tmp)
    tmp = []


# 進む式　x はひとまず0にしている
a = 1
b = 0
x = 0
y = a * x + b


result = hosen(a,b,7)
atmp = result[0]
btmp = result[1]
uz =  riku_range(atmp,btmp,field)
print(uz[0] == [5,9])
# 陸の中で最も直線から距離が離れている座標と長さを知りたい
for i in range(21):
    result = hosen(a,b,i)
    atmp = result[0]
    btmp = result[1]
    uz =  riku_range(atmp,btmp,field)
    if uz[0][0]  == -1:
        continue
    # 今見ている座標から２つの陸の終点の座標の距離をだして
    # i 今見てるx
    # a*i + b 今見てるy
    # uz[0]左側の座標
    # uz[1]右側の座標
    

    # 左の座標との距離を測る
    dxl = uz[0][0] - i
    dyl = uz[0][1] - (a*i + b)
    dl = (dxl**2 + dyl**2)**(1/2)
    dxr = dxl = uz[1][0] - i
    dyr = uz[0][1] - (a*i + b)
    dl = (dxl**2 + dyl**2)**(1/2)
