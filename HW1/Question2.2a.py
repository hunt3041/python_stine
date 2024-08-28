import numpy as np

t = np.linspace(0.1, 0.25, 10)

y = list((6*t**3 - 3*t -4)/(8*np.sin(5*t)))

print(y)