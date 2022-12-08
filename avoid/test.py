# from naname import *
# 被っている陸の範囲でどのくらいの範囲がかぶっているか
import numpy as np
from math import *

field = []
tmp = []
for i in range(10):
    for j in range(10):
        if j > 0 and j < 6 and i > 0 and i < 6:
            tmp.append(1)
        else:
            tmp.append(0)
    field.append(tmp)
    tmp = []


# 指定されたxの範囲にて真ん中から
def hos_range(a,b,x,field,s,e):
    for  i in range(x,s-1,-1):
        y = a * i + b
        y = round(y,4)
        print(a,b,y)
        if y < 0 or y > 20:
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
        print(a,b,y)
        if y < 0 or y > 20:
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
    return result

print(hos_range(-1,6,3,field,1,4))