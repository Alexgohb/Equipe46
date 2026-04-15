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
plt.title("Figure 1: Splines cubiques pour l'EDO implicite")
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.show()

#Question d)

def calcul_max(N):
    coeff = splines_edo_implicite(alpha=alpha_c, beta=beta_c, f=f_c, t0=(np.pi/4), tf=3, N=N)
    t = np.linspace(np.pi/4, 3, N+1)
    y_exact = np.zeros(N+1)
    y_approx = np.zeros(N+1)
    for i, j in enumerate(t):
        y_exact[i] = y(j)
        if i == 0:
            C = coeff[0]
        else:
            C = coeff[i-1]
        y_approx[i] = C[0]*j**3 + C[1]*j**2 + C[2]*j + C[3]
    difference = []
    for i in range(N+1):
        difference.append(abs(y_exact[i] - y_approx[i]))
    return max(difference)

Erreur = np.array([calcul_max(2**6),calcul_max(2**7),calcul_max(2**8),calcul_max(2**9),calcul_max(2**10)])
h = np.array([(3 - np.pi/4) / 2**6, (3 - np.pi/4) / 2**7, (3 - np.pi/4) / 2**8, (3 - np.pi/4) / 2**9, (3 - np.pi/4) / 2**10])

plt.loglog(h, Erreur, 'o-', color='red')
plt.xlabel('h')
plt.ylabel('E(h)')
plt.title('Figure 2: Erreur en fonction de h')
plt.grid(True)
plt.show()

#Question i)

#On défini la fonction f(t, Y) (Y est un vecteur incluant y1 et y2)

f = lambda t, Y:np.array([Y[1], (2*np.exp(-t)/np.sin(t))*Y[0]*Y[1] - 2*np.exp(t)*np.sin(t)])
y0 = np.array([(2**0.5/2)*np.exp(np.pi/4), 2**0.5*np.exp(np.pi/4)])
t, yt = rk4(f, np.pi/4, 3, y0, (3 - np.pi/4)/16)
plt.plot(t, yt[0], label='rk4', color='orange')
plt.plot(np.linspace(np.pi/4, 3, 100), y(np.linspace(np.pi/4, 3, 100)), label='Solution exacte', color='black')
for i in range(len(coeffs) - 1):
    axe_x = np.linspace(t[i], t[i+1], 100)
    C = coeffs[i]
    axe_y = C[0]*axe_x**3 + C[1]*axe_x**2 + C[2]*axe_x + C[3]
    if i == 0:
        plt.plot(axe_x, axe_y, color='red', label='Solution approximation')
    else:
        plt.plot(axe_x, axe_y, color='red')
plt.title("Figure 3: Comparaison des deux méthodes d'approximation et la solution exacte")
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.show()