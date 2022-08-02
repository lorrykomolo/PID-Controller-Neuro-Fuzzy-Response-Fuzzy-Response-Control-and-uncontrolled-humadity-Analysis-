import numpy as np

plt.rcParams["figure.figsize"] = (12,10)
x_pos =2
y_pos =14.25
plt.text(x_pos, y_pos, "FR")

x1_pos =1.83
y1_pos =0.85
plt.text(x1_pos, y1_pos, "PC")

x2_pos =2
y2_pos =21.6
plt.text(x2_pos, y2_pos, "NFR")

x3_pos =2
y3_pos =21.2
plt.text(x3_pos, y3_pos, "PSO")

#import SciPy
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt

# Dataset
x = np.array([0, 0.2, 0.4, 0.6, 0.8, 1, 1.05, 1.1, 1.2, 1.25, 1.35, 1.4, 1.52,1.6, 1.7, 1.8, 2])
y = np.array([11.5, 11.5, 11.5, 11.5, 11.5, 11.5, 13.5, 14.65, 15, 14.6, 14.3, 14.2, 14.25, 14.25, 14.25, 14.25, 14.25])

x1 = np.array([0, 0.2, 0.4, 0.6, 0.8, 1, 1.1, 1.18, 1.2, 1.3, 1.34, 1.4, 1.5, 1.6, 1.65, 1.7, 1.8, 1.82])
y1 = np.array([0, 0, 0, 0, 0, 0, 0.6, 0.96, 1.2, 0.96, 0.8, 0.9, 1, 0.9, 0.85, 0.9, 0.9, 0.84])

x2 = np.array([0, 0.2, 0.4, 0.6, 0.8, 1, 1.02, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.8, 2])
y2 = np.array([20, 20, 20, 20, 20, 20, 20.8, 21.3, 21.6, 21.5, 21.5, 21.5, 21.5, 21.5, 21.5])

x3 = np.array([0, 0.2, 0.4, 0.6, 0.8, 1, 1.02, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.8, 2])
y3 = np.array([20, 20, 20,20, 20, 20, 20.8, 21.4, 21.4, 21.5, 21.5, 21.5, 21.5, 21.5, 21.5])

X_Y_Spline = make_interp_spline(x, y)

X1_Y1_Spline = make_interp_spline(x1, y1)

X2_Y2_Spline = make_interp_spline(x2, y2)

X3_Y3_Spline = make_interp_spline(x3, y3)

# Returns evenly spaced numbers
# over a specified interval.
X_ = np.linspace(x.min(), x.max(), 500)
Y_ = X_Y_Spline(X_)

X1_ = np.linspace(x1.min(), x1.max(), 500)
Y1_ = X1_Y1_Spline(X1_)

X2_ = np.linspace(x2.min(), x2.max(), 500)
Y2_ = X2_Y2_Spline(X2_)

X3_ = np.linspace(x3.min(), x3.max(), 500)
Y3_ = X3_Y3_Spline(X3_)


# Plotting the Graph
plt.plot(X_, Y_,label='FR-Fuzzy Response',color='red')

plt.plot(X1_, Y1_,label='PC-PID Control',color='blue')

plt.plot(X2_, Y2_,label='NFR-Neuro Fuzzy Response',color='green')

plt.plot(X3_, Y3_,label='PSO',color='black')

plt.legend()


plt.box(True)
#plt.plot(X_, Y_, 'x',)


plt.title("GRAPH OF FUZZY RESPONSE, PID CONTROLLER,NEURO FUZZY RESPONSE AND PSO")
plt.xlabel("TIME (s)")
plt.ylabel("RESPONSE")
plt.grid(True)
plt.show()