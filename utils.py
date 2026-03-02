
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

def is_even(n):
    return n % 2 == 0
