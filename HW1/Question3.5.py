import math

def sine_series(x, n):
    if n == 1:
        sin = x
        
    elif n == 2:
        sin = x - x**3/math.factorial(3)
    
    elif n == 3:
        sin = x - x**3/math.factorial(3) + x**5/math.factorial(5) 
    
    elif n == 4:
        sin = x - x**3/math.factorial(3) + x**5/math.factorial(5) - x**7/math.factorial(7) 
    
    elif n == 5:
        sin = x - x**3/math.factorial(3) + x**5/math.factorial(5) - x**7/math.factorial(7) + x**9/math.factorial(9) 
    
    elif n == 6:
        sin = x - x**3/math.factorial(3) + x**5/math.factorial(5) - x**7/math.factorial(7) + x**9/math.factorial(9) - x**11/math.factorial(11)
        
    elif n == 7:
        sin = x - x**3/math.factorial(3) + x**5/math.factorial(5) - x**7/math.factorial(7) + x**9/math.factorial(9) - x**11/math.factorial(11) + x**13/math.factorial(13)
    
    elif n == 8:
        sin = x - x**3/math.factorial(3) + x**5/math.factorial(5) - x**7/math.factorial(7) + x**9/math.factorial(9) - x**11/math.factorial(11) + x**13/math.factorial(13) - x**15/math.factorial(15)
        
    else: 
        return 'number of terms not supported'
    return sin


for i in range(1, 9):
    print(f'Term: {i}, Error: {100 * (math.sin(0.9) - sine_series(0.9, i))/math.sin(0.9)}')
    
