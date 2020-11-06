# =============================================================================
# Practice Mathematical Functions, Strings and Objects
# =============================================================================
import math

print('Contoh 1 : ')
# math functions
a = -3
print(abs(a))       # returns absolute value

a = 3.5
print(abs(-3.5))    # returns absolute value

a = 2
b = 4
c = 1
d = 6
print(max(a, b, c, d))   # returns the max number

print(min(a, b, c, d))  # returns the min number

a = 2
b = 3
print(pow(a, b))

x = 2.5
y = 3.5
print(pow(2.5, 3.5))

x = 3.51
print(round(3.51))

x = 3.4
print(round(x))

x = 3.1456
print(round(x, 2))
print()


print('Contoh 2 : ')
# show math functions using module math


# test algebraic functions
print("exp(1.0) = ", math.exp(1))
print("log(2.78) = ", math.log(2.78))
print("log10 (10, 10) = ", math.log(10, 10))
print("sqrt(4.0) = ", math.sqrt(4.0))
print()

# test trigonometric functions
print("sin (PI / 2) = ", math.sin(math.pi / 2))
print("cos (PI / 2) = ", math.cos(math.pi / 2))
print("tan (PI / 2) = ", math.tan(math.pi / 2))
print("degrees(1.57) = ", math.degrees(1.57))
print("radians(90) = ", math.radians(90))
print()

print("Compute angles")
x1, y1, x2, y2, x3, y3 = float(input("Enter three points : "))

a = math.sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3))
b = math.sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3))
c = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
C = math.degrees(math.acos((c * c - b * b - a * a) / (-2 * a * b)))

print("The three angels are : ", round(A * 100) / 100.0,
      round(B * 100) / 100.0, round(C * 100) / 100.0)
