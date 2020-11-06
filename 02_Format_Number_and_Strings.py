# =============================================================================
# Formating Numbers and Strings
# =============================================================================
print("Contoh 1 :")
amount = 12618.98
interest_rate = 0.0013
interest = amount * interest_rate

print("Interest is", interest)  # print result without formatting number

print("Interest is", round(interest, 2))  # formating number
print("Interest is", format(interest, ".2f"))
print(f"Interest is {interest:.2f}")  # aturan format terbaru
print()

print("Contoh 2 : ")
# Formating floating-point numbers
print(format(57.467657, "10.2f"))
print(format(12345678.923, "10.2f"))
print(format(57.4, "10.2f"))
print(format(57, "10.2f"))

print(format(57.467657, "10.2f"))
print(format(57.467657, ".2f"))
print()

print("Contoh 3 : ")
# Formatting in spesific notation
s = 314.156
print(format(57.467657, "10.2e"))
print(format(0.0033923, "10.2e"))
print(format(57.4, "10.2e"))
print(format(57, "10.2e"))
print(format(s, "10.2e"))
print(f"{s:10.2e}")
print()

print("Contoh 4 : ")
# formatting as a percentage
persen = 0.53457
print(format(0.53457, "10.2%"))
print(format(0.0033923, "10.2%"))
print(format(7.4, "10.2%"))
print(format(57, "10.2%"))
print(f"{persen: 10.2%}")
print(f"{persen: .2%}")
print()

print("Contoh 5 :")
# Justifying format
print(format(57.467657, "10.2f"))
print(format(57.467657, "< 10.2f"))
print(format(57.467657, "< 10.2%"))
print()

print("Contoh 6 :")
# Formatting Integers
integer = 59832
print(format(59832, "10d"))  # integer in decimal number
print(format(59832, "< 10d"))
print(format(59832, "10x"))  # integer in hexadecimal number
print(format(59832, "< 10x"))
print(format(59832, "10o"))  # integer in octal number
print(format(59832, "10b"))  # integer in binary number
print()

print("Contoh 7 : ")
# formatting strings
string = 'Welcome to Python'
print(f"{string:10s} and Java")
print(f"{string:<20s} and Java")
print(f"{string:>20s}")
print(f"{string:>30s} and java")
print()

print("Contoh 8 :")
print(format(57.467657, "9.3f"))
print(format(12345678.923, "9.1f"))
print(format(57.4, ".2f"))
print(format(57.4, "10.2f"))
print()

print("Contoh 9 :")
print(format(57.467657, "9.3e"))
print(format(12345678.923, "9.1e"))
print(format(57.4, ".2e"))
print(format(57.4, "10.2e"))
print()

print("Contoh 10 :")
print(format(5789.467657, "9.3f"))
print(format(5789.467657, "<9.3f"))
print(format(5789.467657, ">9.3f"))
print(format(5789.4, ".2f"))
print(format(5789.4, "<.2f"))
print(format(5789.4, ">9.2f"))
print()

print("Contoh 11:")
print(format(0.457467657, "9.3%"))
print(format(0.457467657, "<9.3%"))
print(format(0.457467657, ">9.3%"))
print()

print("Contoh 12 :")
print(format(45, "5d"))
print(format(45, "<5d"))
print(format(45, ">5d"))
print(format(45, "5x"))
print(format(45, "<5x"))
print(format(45, "5o"))
print(format(45, "<5o"))
print()

print("Contoh 13:")
string = "Programming is fun"
print(f"{string:25s}")
print(f"{string:<25s}")
print(f"{string:>25s}")
