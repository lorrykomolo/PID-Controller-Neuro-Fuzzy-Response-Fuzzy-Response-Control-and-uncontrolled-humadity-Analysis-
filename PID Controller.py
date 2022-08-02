import numpy as np

plt.rcParams["figure.figsize"] = (15,10)
x_pos =1.83
y_pos =0.85
plt.text(x_pos, y_pos, "PC")
#import SciPy
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt

# Dataset
x = np.array([0, 0.2, 0.4, 0.6, 0.8, 1, 1.1, 1.18, 1.2, 1.3, 1.34, 1.4, 1.5, 1.6, 1.65, 1.7, 1.8, 1.82])
y = np.array([0, 0, 0, 0, 0, 0, 0.6, 0.96, 1.2, 0.96, 0.8, 0.9, 1, 0.9, 0.85, 0.9, 0.9, 0.84])

X_Y_Spline = make_interp_spline(x, y)

# Returns evenly spaced numbers
# over a specified interval.
X_ = np.linspace(x.min(), x.max(), 500)
Y_ = X_Y_Spline(X_)

# Plotting the Graph
plt.plot(X_, Y_,color='blue')
plt.box(True)
#plt.plot(X_, Y_, 'x',)
plt.legend(["PC = PID CONTROLLER"], loc ="lower right")
plt.title("PID CONTROLLER")
plt.xlabel("TIME (s)")
plt.ylabel("RESPONSE")
plt.grid(True)
plt.show()