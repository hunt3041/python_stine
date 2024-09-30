import numpy as np

# Define the f_hat(x) approximation for x^0.72
def f_hat(x):
    # Approximation using exponential and logarithm
    return np.exp(0.72 * np.log(x))

# Test case example
x = 5.0  # Replace with any floating point number

# Calculate the true value of x^0.72
true_value = x**0.72

# Calculate the approximate value using f_hat(x)
approx_value = f_hat(x)

# Calculate the relative error
relative_error = abs((approx_value - true_value) / true_value)

# Output the relative error
print(relative_error)
