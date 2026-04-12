import numpy as np
import matplotlib.pyplot as plt
from splines_edo_implicite import splines_edo_implicite
from rk4 import rk4


#Question 1 c)
alpha_c = (np.sqrt(2) * np.exp(np.pi/4))/2
beta_c = (np.sqrt(2) * np.exp(np.pi/4))
f_c = lambda t, y, dy: (2*np.exp(-t) / np.sin(t)) * y * dy - 2*np.exp(t)*np.sin(t)

coeffs = splines_edo_implicite(alpha=alpha_c, beta=beta_c, f=f_c, t0=(np.pi/4), tf=3, N=16)
t = np.linspace(np.pi/4, 3, 17)
y = lambda t: np.exp(t)*np.sin(t)
plt.figure()

for i in range(len(coeffs) - 1):
    axe_x = np.linspace(t[i], t[i+1], 100)
    C = coeffs[i]
    axe_y = C[0]*axe_x**3 + C[1]*axe_x**2 + C[2]*axe_x + C[3]
    if i == 0:
        plt.plot(axe_x, axe_y, color='red', label='Solution approximation')
    else:
        plt.plot(axe_x, axe_y, color='red')
    

y = lambda t:np.exp(t)*np.sin(t)
plt.plot(np.linspace(np.pi/4, 3, 100), y(np.linspace(np.pi/4, 3, 100)), label='Solution exacte', color='black')
plt.title("Splines pour l'EDO implicite")
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.show()
