from math import *
from function import *

# 基本的な値を出しておく
ship = 20 #km/h
Stheta = pi/2
ship_x = ship * cos(Stheta)
ship_y = ship * sin(Stheta)

wind = 10
Wtheta = 0
wind_x = wind * cos(Wtheta)
wind_y = wind * sin(Wtheta)

d = 60

# 船が実際に向く方向を求める

syn_x = ship_x - wind_x
syn_y = ship_y - wind_y

print(syn_x)
print(syn_y)
go_theta = atan(syn_y/syn_x)

dif_theta =kakudo_theta(theta_kakudo(Stheta) - theta_kakudo(go_theta))

real_V = ship * cos(dif_theta)
print(real_V)