import numpy as np 

def arctan4(x, y):
    if x > 0 and y > 0:
        theta = np.arctan(y/x)
    
    elif x < 0 and y > 0:
        theta = np.pi - abs(np.arctan(y/x))
    
    elif x < 0 and y < 0: 
        theta = np.pi + abs(np.arctan(y/x))
    
    elif x > 0 and y < 0:
        theta = 2*np.pi - abs(np.arctan(y/x))
    
    elif x == 0 and y > 0:
        theta = np.pi/2
    
    elif x == 0 and y < 0:
        theta = (3*np.pi)/2
        
    elif x > 0 and y == 0:
        
    return theta
        

