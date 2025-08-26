"""
Given a string b representing a Binary Number, The problem is to find its decimal equivalent.
"""

def convert_binary(b):
    decimal = 0
    for i in range(len(b)):
        binary_digit = int(b[len(b)-1-i])
        decimal += binary_digit * (2**i)

    return decimal

b = "1111"
print(convert_binary(b))
