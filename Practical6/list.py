#make a list of marks
L = [45, 36, 86, 57, 53, 92, 65, 45]
L.sort()
print(L)

#print the boxplot 
import numpy as np
import matplotlib.pyplot as plt
n = 8
score = (45, 36, 86, 57, 53, 92, 65, 45)
plt.title("Rob's marks")
plt.xlabel("score")
plt.boxplot(score, vert=False, whis=1.5, patch_artist=True, meanline=False, showbox=True, showcaps=True, showfliers=True, notch=False, boxprops=dict(facecolor="g"))
plt.show()

#first add the scores together
total = 0
for i in L:
 total += i
#print the average score and compare it with 60
print(total/8)
print("This is lower than the pass mark of 60%")


