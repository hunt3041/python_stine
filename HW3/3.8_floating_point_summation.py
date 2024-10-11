import numpy as np

def accurate_sum(data):
    # Separate positive and negative numbers
    positive_numbers = [num for num in data if num >= 0]
    negative_numbers = [num for num in data if num < 0]

    # Function to perform Kahan summation for better numerical stability
    def kahan_sum(arr):
        data_sum = 0.0  # The sum we'll return
        c = 0.0         # A small correction value

        for value in arr:
            y = value - c       # Subtract the correction from the value
            t = data_sum + y    # Add the corrected value to the running sum
            c = (t - data_sum) - y  # Compute the new correction
            data_sum = t        # Update the running sum

        return data_sum

    # Sum positive and negative numbers separately using Kahan summation
    positive_sum = kahan_sum(positive_numbers)
    negative_sum = kahan_sum(negative_numbers)

    # Combine the two sums
    data_sum = positive_sum + negative_sum

    return data_sum

np.random.seed(42)
data = np.random.randint(-15, 15, 100)
data_sum = accurate_sum(data)
print(data_sum)