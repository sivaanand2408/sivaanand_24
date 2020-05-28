import math
rad_of_circle = float(input())
if rad_of_circle > 0:
    Circum_of_circle = 2 * math.pi * rad_of_circle
    print('%0.2f ' %(Circum_of_circle))
else:
    print('Error')
