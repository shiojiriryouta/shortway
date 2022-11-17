import numpy as np
import math
from geopy.distance import geodesic
import function


start = np.array([32.4194, 132.36768])
end = np.array([35.689096, 135.890086])

# 距離計算
dis = geodesic(start, end).km
print(dis)
dx = end[1] - start[1]

# 角度計算
theta = 90 - math.atan2(math.sin(dx) ,math.cos(start[0])* math.tan(end[0]) - math.sin(start[0]) * math.cos(dx))
print(theta)

# しっかりした角度計算と

lat1 = 35.6544   # 南鳥島の緯度
lon1 = 139.74477 # 南鳥島の経度
lat2 = 121.4225  # 与那国島の緯度
lon2 = 39.8261 # 与那国島の経度

result = function.vincenty_inverse(lat1, lon1, lat2, lon2, 1)

print('距離：%s(m)' % round(result['distance'], 3))
print('方位角(始点→終点)：%s' % result['azimuth1'])
print('方位角(終点→始点)：%s' % result['azimuth2'])

