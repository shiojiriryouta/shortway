import cv2
from photo_route import *
import math
import numpy as np
import matplotlib.pyplot as plt

## 写真にベクトルを描画する
img = cv2.imread("avoid/fig/route2.png")
img2 = img
img_tmp = cv2.flip(img,0)
img_gray = cv2.cvtColor(img_tmp, cv2.COLOR_BGR2GRAY)
ret,img_bi = cv2.threshold(img_gray, 210, 255, cv2.THRESH_BINARY)

# for i in range(img.shape[0]):
#     for j in range(img.shape[1]):
#         if img[i][j][0] == 240 and img[i][j][1] == 199  and img[i][j][2] == 117:
#             img2[i][j] = 255,255,255
#         else:
#             img2[i][j] = 0,0,0


# cv2.imshow("Opencv",img2)
# cv2.waitKey(0)
# cv2.imwrite("avoid/fig/route_test.png", img2)

def cvArrow(img, pt1, pt2, color, thickness=10, lineType=8, shift=0):
    cv2.line(img,pt1,pt2,color,thickness,lineType,shift)
    vx = pt2[0] - pt1[0]
    vy = pt2[1] - pt1[1]
    v  = math.sqrt(vx ** 2 + vy ** 2)
    ux = vx / v
    uy = vy / v
    # 矢印の幅の部分
    w = 10
    h = 20
    ptl = (int(pt2[0] - uy*w - ux*h), int(pt2[1] + ux*w - uy*h))
    ptr = (int(pt2[0] + uy*w - ux*h), int(pt2[1] - ux*w - uy*h))
    # 矢印の先端を描画する
    cv2.line(img,pt2,ptl,color,thickness,lineType,shift)
    cv2.line(img,pt2,ptr,color,thickness,lineType,shift)
pt = np.array([[196,594],[979,570],[1666,559],[1818,516],[1956,385]])
for i in range(4):
    cvArrow(img, pt[i], pt[i+1], (0,255,0), thickness=1, lineType=8, shift=0)

cvArrow(img, pt[0], pt[-1], (0,0,255), thickness=1, lineType=8, shift=0)
# cv2.imshow("Opencv",img)
# cv2.waitKey(0)
# cv2.imwrite("avoid/fig/afterplot.png", img)

## 時間ごとの進む方向と予想時間を出力する
# 潮流のフィールドを定義
sea_flow = []
flow_tmp = []
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        flow_tmp.append([-5,0])
    sea_flow.append(flow_tmp)
    flow_tmp = []



# 距離と時間を求める
pix_d = 18.950 / 1991
des = []
t = []
t_revi = []
vs = 35
for i in range(len(pt) - 1):
    # 座標から座標までの距離を求める
    des_tmp = math.sqrt((pt[i+1][0] - pt[i][0])**2 + (pt[i+1][1] - pt[i][1])**2) * pix_d
    des.append(des_tmp)

    # 船が進む角度を求める
    vec = pt[i+1] - pt[i]

    ship_theta = np.arctan2(vec[1],vec[0])
    print(ship_theta)
    ship_x = vs * math.cos(ship_theta) + sea_flow[pt[i][1]][pt[i][0]][0]
    ship_y = vs * math.sin(ship_theta) + sea_flow[pt[i][1]][pt[i][0]][1]
    revi_theta = np.arctan2(ship_y,ship_x)
    go_x = vs * math.cos(ship_theta) - sea_flow[pt[i][1]][pt[i][0]][0]
    go_y = vs * math.sin(ship_theta) - sea_flow[pt[i][1]][pt[i][0]][1]

    go_theta = np.arctan2(go_y,go_x)
    vs_revi = math.sqrt(ship_x ** 2 + ship_y ** 2)
    vs_norm = abs(vs_revi * math.cos(ship_theta - go_theta))
    print(str(vs_norm) + ' ' + str(vs))
    t_revi_tmp = des_tmp *60 / (vs_norm)
    t_revi.append(t_revi_tmp)
    t_tmp = des_tmp *60 / (vs)
    t.append(t_tmp)
print(des)
print(t)
print(str(sum(des)) + ' km')
print(str(sum(t)) + ' 分')
print(str(sum(t_revi)) + ' 分')

def theta_kakudo(theta):
    pi = math.pi
    return theta*360/(2*pi)

