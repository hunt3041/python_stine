
def rounder(x, n):
    if str(x)[-1] == '5':
        x = x + 0.00000000001
    return round(x, n)

values = [477.9587, 477.958, 7, 0.125, 0.362945, 8192, 135784]
n = [2, 2, 0, 2, 4, -1, -3]

print(list(map(rounder, values, n)))
