import math
def isPowerOfTwo(n):
    if n>0:
        hiBit = math.floor(math.log(n, 2))
        if 2**hiBit==n:
            return True
    return False

print(isPowerOfTwo(0))
