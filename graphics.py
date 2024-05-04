import matplotlib.pyplot as plt
import numpy as np

choice = True
#↑ if you need y graphics type False, if x True
if choice:
    x = np.linspace(-10, 10, 1000)
    y = np.cos(x)
    plt.plot(x, y) 
    plt.title('cos(x) Function Graph')
    plt.xlabel('x')
    plt.ylabel('y')
else:
    y = np.linspace(-10, 10, 1000)
    x = np.cos(y)
    plt.plot(x, y) 
    plt.title('cos(y) Function Graph')
    plt.xlabel('x')
    plt.ylabel('y')

plt.grid(True)
plt.show()
