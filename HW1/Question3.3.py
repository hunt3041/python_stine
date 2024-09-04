import numpy as np

def payment(P, APR, yrs):
    i = APR/(12*100)
    n = yrs*12
    A = P*((i*(1 + i)**n)/((1 + i)**n - 1))
    return A

monthly_payment = payment(40000, 5.3, 3)
print(monthly_payment)