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
    if s != [-1,-1]:
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

#フィールドの定義 陸の範囲 x→j,y→i:5～10
field = []
tmp = []
for i in range(21):
    for j in range(21):
        if j >= 4 and j <= 12 and i >= 2 and i <= 16:
            tmp.append(1)
        else:
            tmp.append(0)
    field.append(tmp)
    tmp = []


# 目的地の座標
fd = [20,20]

# 進む式　x はひとまず0にしている

a = round(fd[1]/fd[0],6)
b = 0
x = 0
y = a * x + b


result = hosen(a,b,8)
atmp = result[0]
btmp = result[1]
uz =  riku_range(atmp,btmp,field)
print(uz)
dxl = uz[0][0] - 8
dyl = uz[0][1] - (a*8 + b)
dl = (dxl**2 + dyl**2)**(1/2)
dxr = uz[1][0] - 8
dyr = uz[1][1] - (a*8 + b)
dr = (dxr**2 + dyr**2)**(1/2)
print(dr,dl)


# 陸の中で最も直線から距離が離れている座標と長さを知りたい
i = 0
dr_max = -1
dl_max = -1
for i in range(21):
    result = hosen(a,b,i)
    atmp = result[0]
    btmp = result[1]
    uz =  riku_range(atmp,btmp,field)
    if uz[0][0]  == -1:
        continue
    # 今見ている座標から２つの陸の終点の座標の距離をだす
    # i 今見てるx
    # a*i + b 今見てるy
    # uz[0]左側の座標
    # uz[1]右側の座標

    yh = atmp*i + btmp
    dxl = uz[0][0] - i
    dyl = uz[0][1] - (a*i + b)
    dl = (dxl**2 + dyl**2)**(1/2)
    dxr = uz[1][0] - i
    dyr = uz[1][1] - (a*i + b)
    dr = (dxr**2 + dyr**2)**(1/2)

    if dr_max < dr :
        dr_max = dr
        rx = uz[0][0]
        ry = uz[0][1]
    if dl_max < dl:
        dl_max = dl
        lx = uz[1][0]
        ly = uz[1][1]  
    i += 1
    y = a * i + b
print(rx,ry,dr_max)
print(lx,ly,dl_max)

if dr_max > dl_max:
    tx = rx
    ty = ry
else:
    tx = lx
    ty = ly

print(tx,ty)
