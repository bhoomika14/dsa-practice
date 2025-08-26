"""
Find n prime numbers using seive of erathosthenes algorithm
"""

# Approach 1 with time complexity O(NrootN)
from math import sqrt
def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, int(sqrt(num))+1):
        if num%i == 0:
            return False
        
    return True

def find_n_primes(n):
    primes = []
    current_num = 2
    while current_num < n:
        if is_prime(current_num):
            primes.append(current_num)
        current_num+=1
    return primes

# Approach 2 using seive of erathosthenes
def prime_numbers(n):
    primes = [True]*n

    for i in range(2, int(sqrt(n))+1):
        if is_prime(i) == True:
            for j in range(i*i, n, i):
                primes[j] = False

    for i in range(2, n):
        if primes[i] == True:
            print(i)

n = 10
prime_numbers(n)
