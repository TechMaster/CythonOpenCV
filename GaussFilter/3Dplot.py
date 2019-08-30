# https://problemsolvingwithpython.com/06-Plotting-with-Matplotlib/06.16-3D-Surface-Plots/

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

x = np.arange(-5, 5, 0.1)

y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x, y)

Z = X * np.exp(-X*X - Y*Y)


fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)
plt.show()
