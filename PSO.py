import numpy as np

plt.rcParams["figure.figsize"] = (15,10)
x_pos =2
y_pos =21.5
plt.text(x_pos, y_pos, "PSO")
#import SciPy
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt

# Dataset
x = np.array([0, 0.2, 0.4, 0.6, 0.8, 1, 1.02, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.8, 2])
y = np.array([20, 20, 20,20, 20, 20, 20.8, 21.4, 21.4, 21.5, 21.5, 21.5, 21.5, 21.5, 21.5])

X_Y_Spline = make_interp_spline(x, y)

# Returns evenly spaced numbers
# over a specified interval.
X_ = np.linspace(x.min(), x.max(), 500)
Y_ = X_Y_Spline(X_)

# Plotting the Graph
plt.plot(X_, Y_,color='black')
plt.box(True)
#plt.plot(X_, Y_, 'x',)
plt.legend(["PSO"], loc ="lower right")
plt.title("PSO")
plt.xlabel("TIME (s)")
plt.ylabel("RESPONSE")
plt.grid(True)
plt.show()
