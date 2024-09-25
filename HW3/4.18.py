import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative
import math

x_value = np.pi/2
def f(x):
    return x - 1 - 0.5*np.sin(x)

def taylor_expansion(x):
    f0 = f(x_value)
    f1 = f0 + derivative(f, x_value, dx=1e-6, n=1)*(x - x_value)
    f2 = f1 + (derivative(f, x_value, dx=1e-6, n=2)/math.factorial(2))*(x - np.pi/2)**2
    f3 = f2 + (derivative(f, x_value, dx=1e-6, n=3)/math.factorial(3))*(x - np.pi/2)**3
    f4 = f3 + (derivative(f, x_value, dx=1e-6, n=4)/math.factorial(4))*(x - np.pi/2)**4
    

def taylor_expansion_plot():
    pass

def taylor_error_plot():
    pass