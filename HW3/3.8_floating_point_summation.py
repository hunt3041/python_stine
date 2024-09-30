import numpy as np

np.random.seed(42)
data = np.random.randint(-15, 15, 100)


def pairwise_sum(arr):
    # If the array is small enough, just sum directly
    if len(arr) < 2:
        return arr.sum()
    # Divide the array into two halves and recursively sum them
    mid = len(arr) // 2
    return pairwise_sum(arr[:mid]) + pairwise_sum(arr[mid:])

# Assuming 'data' is already given as a 1D numpy array
data_sum = float(pairwise_sum(data))

print(type(data_sum))

print(f'Default Sum: {data_sum}, Kahan Sum: {pairwise_sum(data)}')