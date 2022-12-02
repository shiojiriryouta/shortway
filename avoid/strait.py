### これは単に下から上への直線の障害物を避けるプログラムである
import matplotlib.pyplot as plt
import numpy as np
# 船が進む向き
x = [0,0,0,0,1,1,1,0,0,0,0]
y = [0,0,0,0,2,2,2,0,0,0,0]
d = 20
for i in range(8):
    if x[i] == 1:
        s = i
        break

for j in range(s,8):
    if x[j] == 0:
        e = j - 1
        break
print("陸の範囲\nスタート:"+str(s)+'\n終わり:'+str(e))

mv = y[s]
m = s
for i in range(s,e+1):
    if mv < y[i]:
        mv = y[i]
        m = i
print("最高は"+str(m)+"番目の"+str(mv))




### 描画するためのもの
t1 = np.linspace( 0, 20, 40)   # linspace(min, max, N) で範囲 min から max を N 分割します


u2 = ((mv+1)/(m-d))*(t1-d)
u1 = (mv+1)*t1/m


plt.plot(t1,u1)
plt.plot(t1,u2)

plt.show()