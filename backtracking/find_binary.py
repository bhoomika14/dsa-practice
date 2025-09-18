"""
Given an integer N , Print all binary strings of size N which do not contain consecutive 1s.

"""
def findBinary(binary_digits, n):
    if len(binary_digits)==n:
        print(binary_digits, end=" ")
        return
    
    findBinary(binary_digits+"0", n)
    findBinary(binary_digits+"1", n)

def binary(n):
    findBinary("", n)

n = 3
binary(n)