import numpy as np
import matplotlib.pyplot as plt

def y_exact(x):
    return np.exp(-x) - np.exp(-4*x)

x_euler = np.array([
    0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8,
    2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0
])

y_euler = np.array([0, 0.36718885301357923, 0.4665002506843156, 0.4568677620982975, 
                    0.40789991224307565, 0.349250573983921, 0.292849356005355, 
                    0.24288497295918943, 0.2002668947977806, 0.1646013828132104, 
                    0.13505184049999178, 0.11070102550578265, 0.0906930278844929, 
                    0.07427968501243376, 0.06082703970335236, 0.04980637854903207,
                      0.040780457932120685, 0.03338931912165848, 0.02733736114260185, 
                      0.02238216357896741, 0.01832506741963277])

x_fine = np.linspace(0, 4, 400)
y_fine = y_exact(x_fine)

plt.figure(figsize=(8, 5))
plt.plot(x_fine, y_fine, label="Exact solution", linewidth=2)
plt.plot(x_euler, y_euler, 'o-', label="RK4 method (h=0.2)")

plt.xlabel("x($x_n$)")
plt.ylabel("y($Y_n$)")
plt.legend()
plt.grid(True)

plt.show()
