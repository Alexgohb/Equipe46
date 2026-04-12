import numpy as np
import matplotlib.pyplot as plt
from splines_edo_implicite import splines_edo_implicite
from rk4 import rk4


#Question 1 c)
alpha_c = (np.sqrt(2) * np.exp(np.pi/4))/2
beta_c = (np.sqrt(2) * np.exp(np.pi/4))
f_c = lambda x, y, dy: -2*np.exp(-x) / np.sin(x) * y * dy - 2*np.exp(x)*np.sin(x)

coeffs = splines_edo_implicite(alpha=alpha_c, beta=beta_c, f=f_c, t0=(np.pi/4), tf=3, N=16)
t = np.linspace(np.pi/4, 3, 17)
y = lambda t: np.exp(t)*np.sin(t)
plt.figure()
for i in range(len(coeffs)):
    plt.plot(np.linspace(np.pi/4, 3, 17), coeffs[i][0]*t[i]**3 + coeffs[i][1]*t[i]**2 + coeffs[i][2]*t[i] + coeffs[i][3]
    , '-o', label=f'Spline {i}', color = 'orange')

#y = lambda t:np.exp(t)*np.sin(t)
#plt.plot(np.linspace(np.pi/4, 3, 17), y(np.linspace(np.pi/4, 3, 17)), label='Solution exacte', color='black')
#plt.title("Splines pour l'EDO implicite")
#plt.xlabel('t')
#plt.ylabel('y(t)')
plt.show()
