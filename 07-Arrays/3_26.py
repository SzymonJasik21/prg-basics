import matplotlib.pyplot as plt
import numpy as np

degrees = np.arange(0,361,1)
radians = np.deg2rad(degrees)
#x_degrees = np.linspace(0,360,500)
#x_radians = np.deg2rad(x_degrees)

#y = np.sin(x_radians)
y = np.sin(radians)


#plt.plot(x_degrees, y)

plt.plot(degrees, y)
plt.show()

