import re
import sys
from Functions import *


if len(sys.argv) != 2:
    print('hello')
    sys.exit('There are either to little or too many arguments')
    
lhs = []
rhs = []
degree = 0
deg0 = []
deg1 = []
deg2 = []

av = sys.argv[1]
eq = av.split("=")
left = av.split(" ")[0]
right = av.split(" ")[1]
    # calculate(lhs, left)
    # calculate(rhs, right)
conv_sign(rhs)
polynomial = rhs + lhs  
a = ""
b = ""
c = ""
a = deg2
b = deg1
c = deg0
if(degree == 2):
    print("Reduced form: "+a+" + "+b+" + "+c+" = 0")
elif(degree == 1):
    print("Reduced form: "+b+" + "+c+" = 0")
pdeg =  str(degree)
print("polynomial degree: " + pdeg)
if(degree > 2):
    print("The degree should be equal to or less than 2. Your equations could not be solved")
    
a = float(a)
b = float(b)
c = float(c)
discriminant = (b*b) + (4*(a*b))
if(degree == 0):
    if(discriminant == 0):
        print("Only real numbers are permitted in the equation")
    else:
        print("There are solutions for this equation")
discriminant = float(discriminant)
if(degree == 2):
    if(discriminant > 0):
        print("Discriminant is strictly positive. The solutions are:")
    elif(discriminant < 0):
        print("Disriminant is strictly negative. The solutions are:")
            
# if (__name__ == '__main__'):
    # print("hello")
    # main()
