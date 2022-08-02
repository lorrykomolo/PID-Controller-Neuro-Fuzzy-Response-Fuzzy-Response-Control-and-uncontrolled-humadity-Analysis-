import numpy as np

plt.rcParams["figure.figsize"] = (15,10)
x_pos =387
y_pos =47.5
plt.text(x_pos, y_pos, "Controlled")

y1_pos =56.5
plt.text(x_pos, y1_pos, "Uncontrolled")

#import SciPy
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt

# Dataset
x = np.array([0, 50, 100, 150, 200, 250, 300, 350, 400])
y = np.array([45, 47.25, 49.39, 46.49, 46.71, 47.1, 46.91, 47.6, 47.71])

y1 = np.array([45, 47.25, 49.39, 51.03, 53.02, 55.02, 56.01, 56.51, 57.01])

X_Y_Spline = make_interp_spline(x, y)

X1_Y1_Spline = make_interp_spline(x, y1)

# Returns evenly spaced numbers
# over a specified interval.
X_ = np.linspace(x.min(), x.max(), 500)
X1_ = np.linspace(x.min(), x.max(), 500)
Y_ = X_Y_Spline(X_)
Y1_ = X1_Y1_Spline(X1_)

# Plotting the Graph
plt.plot(X_, Y_,label='CONTROLLED',color='blue')

plt.plot(X1_, Y1_,label='UNCONTROLLED',color='red')

plt.box(True)
#plt.plot(X_, Y_, 'x',)
plt.legend()
plt.xlabel("TIME (s)")
plt.ylabel("HUMIDITY")
plt.title("HUMIDITY OF CONTROLLED & UNCONTROLLED")
plt.grid(True)
plt.show()