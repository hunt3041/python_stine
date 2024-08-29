import math

def arctan4(y, x):
    if x < 0 and y > 0:
        theta = math.atan(y/x) + math.pi

    elif x < 0 and y < 0:
        theta = math.atan(y/x) - math.pi

    elif x < 0 and y == 0:
        theta = math.pi

    elif x == 0 and y > 0:
        theta = math.pi/2

    elif x == 0 and y < 0:
        theta = -math.pi/2

    elif x > 0 and y >= 0:
        theta = math.atan(y/x)

    elif x > 0 and y < 0:
        theta = math.atan(y/x)

    else:
        theta = 0
    return theta

