import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from datetime import date

point=[6,7,8,4,8,7,5,4,5,1]

point=np.array(point)
plt.hist(point)
plt.title('客数')
plt.xlabel('日数')
plt.ylabel('客数')
plt.show()

mean=np.mean(point)
std=np.std(point)
print("平均"+str(mean))
print("標準偏差"+str(std))

a=input()
deviation=(int(a)-mean)/std+50

print(date.today())
print("今日の客数の偏差値"+str(deviation))