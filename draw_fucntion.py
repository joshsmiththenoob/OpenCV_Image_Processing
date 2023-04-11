from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection = '3d')
X = np.arange(-5, 5, 0.1)
Y = np.arange(-5, 5, 0.1)
X, Y, = np.meshgrid(X,Y)
R = - X * Y
Z = R / np.e ** (X**2 + Y **2 )
surf = ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = cm.jet, linewidth = 0, antialiased = False)
ax.set_zlim(-1.01, 1.01)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter=(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink = 0.5, aspect = 5)
plt.show()