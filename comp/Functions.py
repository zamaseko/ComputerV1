# import sys
# import re

# def calculator(poly1, poly2):
#     i = 0
#     j = 1
#     poly = poly2
#     while(j < len(poly2)):
#         if(poly2[j] == "+" or poly2[j] == "-"):
#             i += 1
#             poly1[i] = poly2[j]
#         else:
#             if(poly1[i] == "/"):
#                 frac = poly1[i].split("/")
#                 print(frac)
#                 fraction = float(frac[1])
#                 if(fraction == 0):
#                     sys.exit(poly1[i] + ": Number is undefined, The denominator is =")
#                 fraction0 = float(frac[0])
#                 poly1 = str(float(frac[0]) / float(frac[1]))
#             poly1[i] = poly1[i] + poly2[j]
#         j += 1
#     return poly1[i]

# def conv_sign(polyn):
#     i = 0
#     while(i < len(polyn)):
#         if(polyn[i] == "+"):
#             polyn[i] = "-"
#         elif(polyn[i] == "-"):
#             polyn[i] = "+"
#         else:
#             polyn[i] = "-" 
#         i =+ 1
#     return polyn

# def degrees(deg0, deg1, deg2, degs):
#     i = 0
#     power = 0
#     while(i < len(degs)):
#         degree = degs[i].split("^")
#         if(degree == "0"):
#             deg0.append(deg[i])
#         elif(degree == "1"):
#             deg0.append(deg[i])
#         elif(degree == "2"):
#             deg0.append(deg[i])
#         elif(degree[0]):
#             sys.exit("The exponent cannot be negative")
#         elif(degree[1].contains("/")):
#             sys.exit("The fraction cannot have exponents")
#         if(int(degree[1]) > power):
#             power = int(degree[1])
#             print("power check")
            
#             print(power)
#         i += 1
#     if(len(deg0) == 0):
#         deg0.append("0*X^0")
#     elif(len(deg1) == 0):
#         deg1.append("0*X^1")
#     elif(len(deg2) == 0):
#         deg2.append("0*X^2")
#     return power

# def reducer(exp):
#     i = 0
#     tot = 0
#     a =""
#     if(len(exp)):
#         m = exp[i].split("*")
#         while(i < len(exp)):
#             s = exp[i].split("*")
#             ss = float(s[0])
#             tot = tot + ss
#             i += 1
#         t = str(tot)
#         tt = t.split(".")
#         tot = t[i] == "0" and t[0] or tot
#         a = str(tot) + "*" + m[1]
#     return a

# def sqrt(num):
#     abso = 0.000001
#     num = float(num)
#     s = num
#     while((s-num/s) > abso):
#         s = (s + num / s) /2
#     return s

