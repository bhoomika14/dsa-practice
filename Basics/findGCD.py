def find_gcd(a, b):
    if a%b == 0:
        return b
    return find_gcd(b, a%b)

a = 20, b= 28
print(f"GCD of {a}, {b} is {find_gcd(a, b)}")


