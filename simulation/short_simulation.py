import numpy as np
import matplotlib.pyplot as plt
import math

# 地図配列ダミーデータ20✕10
coodinate = []
itigyou = []
lat = 34.200
lng = 133.600
for i in range(10):
    for j in range(20):
        tmp = [round(lat,2),round(lng,2),-5,4]
        itigyou.append(tmp)
        lng +=  0.04000
    lat += 0.04000
    coodinate.append(itigyou)
    itigyou = []

print(coodinate[0][5])


# πの値を角度(°)に変換
def theta_kakudo(theta):
    pi = math.pi
    return theta*360/(2*pi)


# スタート地点の座標の定義
start_lat = 34.2
start_lng = 133.6


def vector_plot(v_ship,theta_ship,v_wind,theta_wind):

    plt.figure()
    #船のベクトルを出す
    
    vx_ship = v_ship * math.cos(theta_ship)
    vy_ship = v_ship * math.sin(theta_ship)
    plt.quiver(0,0,vx_ship,vy_ship,color = 'blue',angles='xy',scale_units='xy',scale=1)
    # 上の0,0を最初の座標に変換する

    #風のベクトルを出す

    
    vx_wind = v_wind * math.cos(theta_wind)
    vy_wind = v_wind * math.sin(theta_wind)
    wind_vector_x = vx_ship + vx_wind
    wind_vector_y = vy_ship + vy_wind
    plt.quiver(vx_ship,vy_ship,vx_wind,vy_wind,color = 'green',angles='xy',scale_units='xy',scale=1)

    #合成ベクトルを出す

    plt.quiver(0,0,wind_vector_x,wind_vector_y,color = 'red',angles='xy',scale_units='xy',scale=1)
    # 上の0,0を最初の座標にする
    plt.xlim([-10,100]) #図のxの範囲
    plt.ylim([-10,100]) #図のyの範囲
    plt.grid() #図の中に縦と横の線を引く
    plt.show() #図を表示