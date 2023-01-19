from geo_theta_norm import *

# スタート地点の座標
lat1 = 34.353227662632804
lon1 = 134.040005946406 
lat2 = 34.379795948823656 
lon2 = 134.03838605050075 

result = vincenty_inverse(lat1, lon1, lat2, lon2, 1)
go_theta = result['azimuth1'] - 270
back_theta = result['azimuth2'] + 90
print(go_theta)
print('距離：%s(m)' % round(result['distance'], 3))
print('方位角(始点→終点)：%s' % go_theta)
print('方位角(終点→始点)：%s' % back_theta)

