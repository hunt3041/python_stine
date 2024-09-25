import math
import numpy as np

def maclaurin_cos(x, tol=1e-6, maxit=50):
    """
    Maclaurin series expansion for cos(x) 

    Args:
        x (double): Value to evaluate at
        es (double, optional): Max error allowed. Defaults to 1e-4.
        maxit (int, optional): Max iterations allowed. Defaults to 50.

    Returns:
        fx (double): Maclaurin series approximation
        ea (double): Approximate relative error
        iter (int): Number of iterations taken to reach desired relative error.
    """
    iter = 1 
    sol = 1
    ea = 100
    while True:
        solold = sol
        sol = sol + (-1)**iter*(x**(2*iter)/math.factorial(2*iter))
        iter = iter + 1

        if sol != 0:
            ea = abs((sol - solold)/sol)*100
        if ea < tol or iter >= maxit:
            break
    fx = sol
    return fx, ea, iter


result_pi_over_3, error1, iter1 = maclaurin_cos(math.pi/3, 1e-6)
result_7pi_over_3, error2, iter2 = maclaurin_cos((7*math.pi)/3, 1e-6)

print(f'Estimated: {result_pi_over_3}, Actual: {np.cos(math.pi/3)}')
print(f'Estimated: {result_7pi_over_3}, Actual: {np.cos((7*math.pi)/3)}')