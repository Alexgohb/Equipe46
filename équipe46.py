import numpy as np
import matplotlib.pyplot as plt
from splines_edo_implicite import splines_edo_implicite
from rk4 import rk4


#Question 1 c)
alpha_c = (np.sqrt(2) * np.exp(np.pi/4))/2
beta_c = (np.sqrt(2) * np.exp(np.pi/4))
f_c = lambda x, y, dy: -2*np.exp(-x) / np.sin(x) * y * dy - 2*np.exp(x)*np.sin(x)

print(splines_edo_implicite(alpha=alpha_c, beta=beta_c, f=f_c, t0=(np.pi/4), tf=3, N=16))

