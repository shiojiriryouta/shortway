import numpy as np
import matplotlib.pyplot as plt
import math

plt.figure()

pi = math.pi

#船のベクトルを出す
v_ship = 37.5
theta_ship = pi/4
vx_ship = v_ship * math.cos(theta_ship)
vy_ship = v_ship * math.sin(theta_ship)
plt.quiver(0,0,vx_ship,vy_ship,color = 'blue',angles='xy',scale_units='xy',scale=1)

#風のベクトルを出す

v_wind = 10
theta_wind = 3*pi/2
vx_wind = v_wind * math.cos(theta_wind)
vy_wind = v_wind * math.sin(theta_wind)
wind_vector_x = vx_ship + vx_wind
wind_vector_y = vy_ship + vy_wind
plt.quiver(vx_ship,vy_ship,vx_wind,vy_wind,color = 'green',angles='xy',scale_units='xy',scale=1)

#合成ベクトルを出す

plt.quiver(0,0,wind_vector_x,wind_vector_y,color = 'red',angles='xy',scale_units='xy',scale=1)

# 進みたい方向はπ/4 の方向
tany = vy_ship - vy_wind
tanx = vx_ship - vx_wind
theta_adjast = math.atan(tany/tanx)

vx_ship = v_ship * math.cos(theta_ship)
vy_ship = v_ship * math.sin(theta_ship)


# グラフ表示
plt.xlim([-10,40]) #図のxの範囲
plt.ylim([-10,40]) #図のyの範囲
plt.grid() #図の中に縦と横の線を引く
plt.show() #図を表示