import cv2
from photo_route import *
import math
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
pt = [[196,594],[979,570],[1666,559],[1818,516],[1956,385]]
for i in range(4):
    cvArrow(img, pt[i], pt[i+1], (0,255,0), thickness=1, lineType=8, shift=0)

cvArrow(img, pt[0], pt[-1], (0,0,255), thickness=1, lineType=8, shift=0)
cv2.imshow("Opencv",img)
cv2.waitKey(0)
cv2.imwrite("avoid/fig/afterplot.png", img)

fd = [2269,455]

# print(turn_point(sd,fd,img_bi))


