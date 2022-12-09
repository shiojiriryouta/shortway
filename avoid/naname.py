import matplotlib.pyplot as plt
import numpy as np
from math import *

# 出発地と目的地から傾きと切片を求める
def kase(sd,fd):
    a = (fd[1] - sd[1])/(fd[0] - sd[0])
    b = sd[1] - a * sd[0]
    result = [a,b]
    return result

# 法線を求める関数 ax+bに垂直で点(c,ac+b)を通る法線の関数
def hosen(a,b,c):
    ah = -1/a
    bh = c/a + a*c + b
    return ah,bh

# 船の目的地への直線と被っている陸の範囲を表示する関数(ただ後ろにも反応してしまう)
def riku_range(a,b,field):
    s = [-1,-1]
    e = [-1,-1]
    for  i in range(201):
        y = a * i + b
        y = round(y,7)
        if y < 0 or y > 200:
            continue
        # 傾きが正なら切り捨てて負なら切り上げる(eでは逆)
        if np.sign(a) == 1:
            y = floor(y)
        else:
            y = ceil(y)
        if field[y][i] == 1 and [i,y] != sd:
            s = [i,y]
            break
    
    if s != [-1,-1]:
        for i in range(s[0],201):
            y = a * i + b
            y = round(y,7)
            if y < 0 or y > 200:
                continue
            if np.sign(a) == 1:
                y = ceil(y)
            else:
                y = floor(y)
            if field[y][i] == 0:
                e = [i-1,round(a * (i-1) + b)]
                break
    return s,e

# riku_rangeを法線で使うときの範囲指定版関数
def hos_range(a,b,x,field,s,e):

    if x >= s and e >= x:

        for  i in range(x,s-1,-1):
            y = a * i + b
            y = round(y,4)
            
            if y < 0 or y > 200:
                break
            if np.sign(a) == 1:
                y = floor(y)
            else:
                y = ceil(y)
            if field[y][i] == 1:
                ans = [i,y]
            else:
                break
        result = [ans]
        for i in range(x,e+1):
            y = a * i + b
            y = round(y,4)
            
            if y < 0 or y > 200:
                break
            if np.sign(a) == 1:
                y = floor(y)
            else:
                y = ceil(y)
            if field[y][i] == 1:
                ans = [i,y]
            else:
                break
        result.append(ans)
    else:
        result = [[-1,-1],[-1,-1]]
    
    return result

# 出発地と目的地その他もろもろを入れるとどこに向かうべきか出力してくれる関数を定義する

def turn_point(sd: list,fd: list,field: list):
    
    # 進む式の係数を求めている y = ax + b
    a = (fd[1] - sd[1])/(fd[0] - sd[0])
    b = sd[1] - a * sd[0]
    
    # 陸の中で最も直線から距離が離れている座標と長さを知りたい
    dr_max = dl_max = -1
    lx = ly = rx = ry = None
    for i in range(sd[0],fd[0]+1):
        
        # 法線を出して陸の範囲を出す
        ho = hosen(a,b,i)
        atmp = ho[0]
        btmp = ho[1]
        uzb = riku_range(a,b,field)
        uz =  hos_range(atmp,btmp,i,field,uzb[0][0],uzb[1][0])
        if uz[0][0]  == -1 and uz[1][0] == -1:
            continue

        # 今見ている座標から２つの陸の終点の座標の距離をだす
        # i 今見てるx
        # a*i + b 今見てるy
        # uz[0]左側の座標
        # uz[1]右側の座標


        dxl = uz[0][0] - i
        dyl = uz[0][1] - (a*i + b)
        dl = (dxl**2 + dyl**2)**(1/2)
        dxr = uz[1][0] - i
        dyr = uz[1][1] - (a*i + b)
        dr = (dxr**2 + dyr**2)**(1/2)

        # 左右の距離の最大を求める
        if dr_max < dr :
            dr_max = dr
            rx = uz[1][0]
            ry = uz[1][1]
        if dl_max < dl:
            dl_max = dl
            lx = uz[0][0]
            ly = uz[0][1]  

    # 2つのMAXで小さい方の座標を取得する

    # if dr_max > dl_max:
    #     tx = lx
    #     ty = ly
    # else:
    #     tx = rx
    #     ty = ry

    result = []

    if lx == None and ry == None:
        result.append(fd)
        result.append(fd)
    else:
        result.append([lx,ly])
        result.append([rx,ry])
    return result

#フィールドの定義 陸の範囲 x→j,y→i:5～10
field = []
tmp = []
for i in range(201):
    for j in range(201):
        if j >= 40 and j <= 140 and i >= 20 and i <= 160:
            tmp.append(1)
        else:
            tmp.append(0)
    field.append(tmp)
    tmp = []

for i in range(20,60):
    for j in range(81,141):
        field[i][j] = 0

# 出発地，目的地の座標
sd = [0,0]
fd = [140,60]

ab = kase(sd,fd)
tyoku = riku_range(ab[0],ab[1],field)
test = turn_point(sd,fd,field)
if tyoku == ([-1,-1],[-1,-1]) or tyoku[0] == tyoku[1] or test[0] == test[1]:
    
    print(f"{sd} → {fd}")
else:
    print(test)

# # # 目的地が出力されるまで求め続ける

# sd = test[0]
# a = (fd[1] - sd[1])/(fd[0] - sd[0])
# b = sd[1] - a * sd[0]



# c = riku_range(a,b,field)
# if c[0] == c[1]:
#     print(fd)


# sd = test[1]
# a = (fd[1] - sd[1])/(fd[0] - sd[0])
# b = sd[1] - a * sd[0]

# c = riku_range(a,b,field)
# if c[0] == c[1]:
#     print(fd)
