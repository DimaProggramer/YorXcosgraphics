import matplotlib.pyplot as plt
import numpy as np

range_values = np.linspace(-10, 10, 1000)

fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(range_values, np.cos(range_values))
axs[0, 0].set_title('cos(x)')
axs[0, 0].grid(True)

axs[0, 1].plot(np.cos(range_values), range_values)
axs[0, 1].set_title('cos(y)')
axs[0, 1].grid(True)

axs[1, 0].plot(range_values, np.tan(range_values))
axs[1, 0].set_title('tan(x)')
axs[1, 0].grid(True)

axs[1, 1].plot(np.tan(range_values), range_values)
axs[1, 1].set_title('tan(y)')
axs[1, 1].grid(True)

plt.tight_layout()
plt.show()
