import re
import sys

def poly_deg(leq):
    power = 0
    i = 0
    while(i < len(leq)):
        if(leq[i] == "^"):
            power = int(leq[i + 1])
            if(power > 2):
                sys.exit("The polynomial degree cannot be greater than 2")
        i += 1
    return power

def to_float(string):
    s = " "
    if(s == str()):
        s = float(s)
        print(s)
    return s

def sqrt(num):
    abso = 0.000001
    num = float(num)
    s = num
    while((s-num/s) > abso):
        s = (s + num / s) /2
    return s

# def side(left, right):
#     hold = right
#     right = left
#     left = hold

#     ls = left.split(" ")
#     rs = right.split(" ")
#     j = 2
#     for d in ls and rs:
#         if((j - 2) < len(rs) and (j - 2) < len(ls)):
#             if ((j - 2) < len(rs) and (j - 2) < len(ls)):
#                 if (d == "X^0" or d == "X^1" or d == "X^2"):
#                     hold = float(rs[j - 4]) * -1
#                     ls[j - 4] = str(float(left[j - 4]) + hold)
#             j += 1
#         final = " ".join(ls)
#         # final_eq = final.split(' ')
#         print("check reduced")
#         print(final)
        
#     return final

def solve():
    if(len(sys.argv) != 2):
        sys.exit("Only one argument is permitted")
    pd = 0
    formula = sys.argv[1].upper().split(' = ')
    lhs = formula[0]
    rhs = formula[1]
    pd = poly_deg(lhs)
    left = lhs.split(' ')
    right = rhs.split(' ')
    equat = left + right
    
    i = 0
    while(i < len(right)):
        if(right[0] == "+"):
            right[i] = "-"
        elif(right[i] == "-"):
            right[i] = "+"

        i += 1
    
    
    # i = 0
    # final_split = final.split(" ")
    # print(final_split)
    # while(i < len(left)):
    #     if (final_split[i] == "X^0"):
    #         c = float(final_split[i - 2])
    #         print("check c")
    #         print(c)
    #     if (final_split[i] == "X^1"):
    #         if (final_split[i - 3] != "-"):
    #             b = float(final_split[i - 2])
    #             print("check b")
    #             print(b)  
    #         else:
    #             b = float(final_split[i - 2]) * -1
    #     if (final_split[i] == "X^2"):
    #         if (final_split[i - 3] != "-"):
    #             a = float(final_split[i - 2])
    #             print("check a")
    #             print(a)
    #         else:
    #             a = float(final_split[i - 2]) * -1
    #     i += 1

    if(pd == 2):
        print("Reduced form: " + "= 0" )
    elif(pd == 1):
        print("Reduced form: " + "= 0" )
    print("Polynomial degree: " + str(pd))
    if(pd > 2):
        sys.exit("The polynomial degree cannot br greater that 2")

    discriminant = (b * b) - (4 *(a * c))
    if(pd == 0):
        if(discriminant == 0):
            sys.exit("The equation only takes in real numbers")
        else:
            sys.exit("NO real solutions")
    
    discriminant = float(discriminant)
    if(pd == 2):
        if(discriminant > 0):
            print("Strictly positive discriminant. Solutions: ")
        elif(discriminant < 0):
            print("Strictly negative discriminant. Solution: ")
            print(solution2)
        else: 
            print("The discriminant is zero. The solution is: ")
            solution = (- b -sqrt(discriminant)) / (2 * a)
            sys.exit(str(solution))
        solution1 = (-b - sqrt(discriminant)) / (2 * a)
        solution2 = (-b + sqrt(discriminant)) / (2 * a)

        print(solution1)
        print(solution2)    
    elif(power == 1):
        solution = -c/b
        print(solution)

solve()