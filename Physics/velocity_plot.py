import numpy as np
import matplotlib.pyplot as plt
import math

def theta_kakudo(theta):
    pi = math.pi
    return theta*360/(2*pi)

plt.figure()

pi = math.pi

#船の速度定義
v_ship = 37.5
theta_ship = pi/4

#船の速度をxとyに分ける
vx_ship = v_ship * math.cos(theta_ship)
vy_ship = v_ship * math.sin(theta_ship)

#船のベクトル定義
plt.quiver(0,0,vx_ship,vy_ship,color = 'blue',angles='xy',scale_units='xy',scale=1)


#風の速度定義
v_wind = 10
theta_wind = 3*pi/2

#風をxとyに分ける
vx_wind = v_wind * math.cos(theta_wind)
vy_wind = v_wind * math.sin(theta_wind)

# 風と船の速度をx,yごとに合成
wind_vector_x = vx_ship + vx_wind
wind_vector_y = vy_ship + vy_wind

#風のベクトル定義
plt.quiver(vx_ship,vy_ship,vx_wind,vy_wind,color = 'green',angles='xy',scale_units='xy',scale=1)

#合成ベクトル定義
plt.quiver(0,0,wind_vector_x,wind_vector_y,color = 'red',angles='xy',scale_units='xy',scale=1)

# 
tany = vy_ship - vy_wind
tanx = vx_ship - vx_wind
theta_adjast = math.atan(tany/tanx)
print(theta_adjast)
print(theta_kakudo(theta_adjast))

# グラフ表示
plt.xlim([-10,100]) #図のxの範囲
plt.ylim([-10,100]) #図のyの範囲
plt.grid() #図の中に縦と横の線を引く
plt.show() #図を表示