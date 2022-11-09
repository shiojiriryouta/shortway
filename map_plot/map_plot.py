import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cv2

# 画像のサイズを確認
pic = cv2.imread("map_plot/images/03_2022110223.png")
print(pic.shape)

# グラフの縦横比を設定
fig = plt.figure(figsize=(8, 6))
# 背景を白にする(上に画像が乗るので関係ない)
fig.patch.set_facecolor('white')
# グラフを表示させる位置を設定
ax = fig.add_subplot(1, 1, 1)

x = [0, 1016, 0]
y = [0, 703, 0]

# タッチ座標をプロットする
for  i in range(0,pic.shape[0],50):
    for j in range(0,pic.shape[1],50):
        x[2] = j
        y[2] = i
        ax.scatter(x, y, c='red', s=10,marker="$|$")

# 画像データを変数に代入
im = Image.open("map_plot/images/03_2022110223.png")

ax.imshow(im , alpha=0.6)

plt.show()