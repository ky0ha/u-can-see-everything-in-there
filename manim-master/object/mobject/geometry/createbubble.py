import matplotlib.pyplot as plt 
import numpy as np

line_dict = {
    "color" : "k",
    "linewidth" : 2.0
}

angle_range = np.linspace(-120, 220) * np.pi / 180.
x = 3 * np.cos(angle_range)
y = 2 * np.sin(angle_range)

x, y = x.tolist(), y.tolist()
x = x + [-3 * 1.2, x[0]]
y = y + [-2 * 1.2, y[0]]

plt.plot(x, y, **line_dict)
plt.axis("off")
plt.savefig("./images/bubble.svg")