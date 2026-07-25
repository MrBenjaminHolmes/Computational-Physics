from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


data = np.loadtxt("Resources/stm.txt", float)
plt.imshow(data, cmap='gray')
plt.title("STM Density Plot")
plt.show()