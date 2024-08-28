import numpy as np

def tank_volume(R, d):
    if d <= R:
        volume = (np.pi*R**2*d)/3
    
    elif R < d <= 3*R:
        volume = (np.pi*R**3)/3 + np.pi*R**2*(d)
    
    else:
        volume = 'Overtop'
    
    return volume

test_vector = ((.9, 1), (1.5, 1.25), (1.3, 3.8), (1.3, 4.0))

for test_point in test_vector:
    print(tank_volume(test_point[0], test_point[1]))
