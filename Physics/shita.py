import numpy as np
import math
from geopy.distance import geodesic

departure = np.array([1,1])
destination = np.array([2,2])
# 座標間のベクトルの大きさを計算
distance = np.linalg.norm(departure - destination)
vec = destination - departure
shita = np.arctan2(vec[0],vec[1])
print(shita)
print(np.sin(shita))
print(1/math.sqrt(2))

TokyoStation = (35.681382, 139.76608399999998)
NagoyaStation = (35.170915, 136.881537)
print(type(TokyoStation))

dis = geodesic(TokyoStation, NagoyaStation).km

print(dis)

pi = math.pi
kakudo = shita*360/(2*pi)
print(kakudo)