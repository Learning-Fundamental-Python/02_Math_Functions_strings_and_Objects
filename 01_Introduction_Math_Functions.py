##################################################
# Introduction functions, strings and objects
# in Python Programs
##################################################
import math

print("Common Python Function : ")
# Python provides many useful functions
# for common programming task
print(f"abs(-3) = {abs(-3)}")                           # Returning the absolut value
print(f"abs(-3.5) = {abs(-3.5)}")
print(f"max(2, 3, 4, 5, 6) = {max(2, 3, 4, 5, 6)}")     # Returning the maximum value
print(f"min(2, 3, 4, 5, 6) = {min(2, 3, 4, 5, 6)}")     # Returning the minimum value
print(f"pow(2, 3) = {pow(2, 3)}")                       # same as 2 ** 3
print(f"pow(2.5, 3.5) = {pow(2.5, 3.5):.3f}")           # same as 2.5 ** 3.5
print("round(3.56565) = ", round(3.56565))              # Rounds to its nearest integer
print("round(3.56565, 2) = ", round(3.56565, 2))        # Rounds to 3 digits after the decimal point

# Mathematical Functions
# The math functions defined in the 'math module'
# Test algebraic functions
print(f"Nilai Pi = {math.pi}")
print(f"exp(1.0) = {math.exp(1)}")
print(f"log(2.78) = {math.log(math.e)}")
print(f"log10(10, 10) = {math.log(10, 10)}")
print(f"sqrt(4.0) = {math.sqrt(4.0)}")

# Test trigonometric functions
print("sin(PI / 2) = ", math.sin(math.pi / 2))
print("cos(PI / 2) = ", math.cos(math.pi / 2))
print(f"tan (PI / 2) = {math.tan(math.pi / 2)}")
print(f"degrees(1.57) = {math.degrees(1.57)}")          # Conversion value from radians to degrees
print(f"radians(90) = {math.radians(90)}")              # Conversion value from degrees to radians
