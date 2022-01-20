import matplotlib.pyplot as plt
import numpy as np

x = np.array([3,6,6,25,35,45,1,4])
mylabels = ["civil","mech","ee","ec","cse","ise","bt","mca"]#graph label

plt.pie(x,labels = mylabels)#angle setup
plt.show()

x.sort()
print(x[-1])