import re
import sys

# Check it the etion has a polynomial and check if the polynomial is lesser than or equal to 2
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

# the squareroot function for the quadratic equation discriminant
def sqrt(num):
    abso = 0.000001
    num = float(num)
    s = num
    while((s-num/s) > abso):
        s = (s + num / s) /2
    return s

# convert the signs and simplify the equation by add/subtracting like terms to get a reduced form of the equation given 
def simplify(poly):
    left = poly.split(" = ")[0]
    right = poly.split(" = ")[1]
    rs = right.split(" ")
    if (rs[0] == "-"):
        rs[0].index("+")
    else:
        rs.insert(0, "-")
    i = 1
    while (i < len(rs)):
        if (rs[i] == "+"):
            rs[i] = "-"
        elif (rs[i] == "-"):
            rs[i] = "+"
        i += 1 
    changed_poly = left + " " + " ".join(rs)
    rs = changed_poly.split(" ")
    if (rs[0] != "-"):
        rs.insert(0, "+")
    i = 3
    j = i + 4
    while (i < len(rs)):
        while (j < len(rs)):
            if (rs[i] == rs[j]):
                if(rs[i - 3] == "+"):
                    temp = float(rs[i -2])
                else:
                    temp = rs[i - 2] * 1
                if(rs[j - 3] == "+"):
                    temp = float[j - 2]
                else:
                    temp = temp - float(rs[j - 2])
                if (temp < 0):
                    rs[i - 3] = "-"
                    rs[i - 2] = str(temp * -1)
                else:
                    rs[i - 3] = "+"
                    rs[i - 2] = str(temp)
                rs = rs[:j - 3] + rs[j + 1:]
                j -= 4
            j += 4
        i += 4
        j = i + 4
    if (rs[0] != "-"):
        rs.pop(0)
    reduced_poly = " ".join(rs)
    return (reduced_poly)

# Once the equation has been handle this solves quadratic equation and breaks down 
def solve():
    if(len(sys.argv) != 2):
        sys.exit("Only one argument is permitted")
    pd = 0
    equation = sys.argv[1]
    formula = sys.argv[1].split(' = ')
    lhs = formula[0]
    rhs = formula[1]
    pd = poly_deg(lhs)
    left = lhs.split(' ')
    right = rhs.split(' ')
    equat = left + right
    eq = simplify(equation)
    i = 0
    reduction = eq.split(" ")
    while(i < len(left)):
        if (reduction[i] == "X^0"):
            c = float(reduction[i - 2])
        if (reduction[i] == "X^1"):
            if (reduction[i - 3] != "-"):
                b = float(reduction[i - 2])
            else:
                b = float(reduction[i - 2]) * -1
        if (reduction[i] == "X^2"):
            if (reduction[i - 3] != "-"):
                a = float(reduction[i - 2])
            else:
                a = float(reduction[i - 2]) * -1
        i += 1

    if(pd == 2):
        print("Reduced form: " + eq + " = 0" )
    elif(pd == 1):
        print("Reduced form: " + eq + " = 0" )
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
            print("Strictly positive discriminant. your solutions are: ")
        elif(discriminant < 0):
            print("Strictly negative discriminant. Your solutions are: ")
        else: 
            print("The discriminant is zero. The solution is: ")
            solution = (- b -sqrt(discriminant)) / (2 * a)
            sys.exit(str(solution))
        solution1 = (-b - sqrt(discriminant)) / (2 * a)
        solution2 = (-b + sqrt(discriminant)) / (2 * a)

        print(solution1)
        print(solution2)    
    elif(pd == 1):
        solution = -c/b
        print(solution)

solve()