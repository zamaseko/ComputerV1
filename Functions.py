import re 
import sys

def sqrt(num):
    deg = 0.0000001
    num = float(num)
    n = num
    while (n - num/n) > deg:
        n = (n + num / n)/2
    return n

def sqr_nums(num):
    return num * num

def conv_sign(sign):
    i = 1
    while(i < len(sign)):
        if(sign[1] == '-'):
            sign[i] == '+'
        if(sign[i] == '+'):
            sign[i] == '-'
        i += 1