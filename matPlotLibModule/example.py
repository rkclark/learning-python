from matplotlib import pyplot as plt
import numpy as np

x, y = np.loadtxt("./matPlotLibModule/data.txt", unpack=True, delimiter=",")

plt.style.use("seaborn-dark")
plt.plot(x, y)

plt.title("Awesome chart")
plt.ylabel("Y axis")
plt.xlabel("X axis")

plt.show()
