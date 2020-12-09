import sys
import re

#solver must 

#squareroot table gives squareroot degree number as 0.0000001
def sqrt(num):
    deg = 0.0000001
    num = float(num)
    n = num
    while((n - num/n) > deg):
        n = (n + num / n)/2
    print(n)

sqrt(25)