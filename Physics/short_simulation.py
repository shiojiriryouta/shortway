import numpy as np
import matplotlib.pyplot as plt
from math import *
from function import *

## 地図配列ダミーデータ20✕10を作成
coodinate = []
itigyou = []
# 左下の座標
lat = 34.200 
lng = 133.600
# 何個範囲内の座標をどのくらい分割するか (sep-1 が分割する数)
sep_lat = 11
sep_lng = 21

for i in range(sep_lat):
    for j in range(sep_lng):
        tmp = [round(lat,2),round(lng,2),-5,4]
        itigyou.append(tmp)
        lng +=  0.04000
    lat += 0.04000
    lng = 133.600
    coodinate.append(itigyou)
    itigyou = []


# 出発地の座標と近いマッピングの座標を出力する
in_lat = 34.44554
in_lng = 133.94749
for  i in range(10):
    if in_lat < 34.2 or in_lat > 34.6 or in_lng < 133.6 or in_lng > 134.4 :
        print("入力座標が範囲外です")
        break
    if 34.2 + i * (0.4/(sep_lat-1)) >= in_lat :
        ans_lat = i
        break

for i in range(20):
    if in_lat < 34.2 or in_lat > 34.6 or in_lng < 133.6 or in_lng > 134.4 :
        print("入力座標が範囲外です")
        break
    if 133.6 + i * (0.8/(sep_lng-1)) >= in_lng :
        ans_lng = i
        break

## 妨害要素を考慮して進行方向を出力

#目的地の座標
des_lat = 34.5
des_lng = 134.2

go_kakudo = vincenty_inverse(ans_lat, ans_lng, des_lat, des_lng, 1)['azimuth1']
go_theta = kakudo_theta(go_kakudo)

v_ship = 35
cood_tmp = coodinate[ans_lat][ans_lng]
v_wind = ( cood_tmp[2] ** 2 + cood_tmp[3] ** 2 ) ** (1/2)
theta_wind = atan(cood_tmp[3]/cood_tmp[2]) + pi
vector_plot(v_ship,go_theta,v_wind,theta_wind)

ds = vincenty_inverse(34.133543,133.532333,34.563754,134.099271,1)

print(ds)
