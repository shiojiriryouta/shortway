# 出発地、目的地、フィールドの潮流、フィールドの風の力、船の速さ、の5つを与えると角度調整をした方向が表示される関数を作成
from math import *
import numpy as np
# 出発地、目的地、フィールドの潮流、フィールドの風の力、船の速さを定義
sd = np.array([0,0])
fd = np.array([50,50])
wind_field = np.array([])
wind_tmp = []
for i in range(201):
    for j in range(201):
        x = -5
        y = -4

        wind_tmp.append([x,y])
    wind_field.append(wind_tmp)
    wind_tmp = []
flow_field = []
flow_tmp = []
for i in range(201):
    for j in range(201):
        x = -2
        y = -3

        flow_tmp.append([x,y])
    flow_field.append(flow_tmp)
    flow_tmp = []
vs = 30 # [km/h]


# 出発地から目的地までの角度を求める
dx = fd[0] - sd[0]
dy = fd[1] - sd[1]
thsh = atan2(dy,dx)

# 潮流を差し引いた進むべき方向を求める
rex = vs*cos(thsh) - flow_field[sd[1]][sd[0]][0]
rey = vs*sin(thsh) - flow_field[sd[1]][sd[0]][1]

reth = atan2(rey,rex)

# 船の進む方向と風の服方向のなす角

print(degrees(reth))

shipw = 3.2
shipl = 10
shiph = 2



