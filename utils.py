def sum_digits(n: int) -> int:
    n = abs(n)
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s
def is_power_of_two(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0

def lcm(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    if a == 0 or b == 0:
        return 0
    # gcd inline to avoid dependency
    x, y = a, b
    while y:
        x, y = y, x % y
    return a // x * b

