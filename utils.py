def sum_digits(n: int) -> int:
    n = abs(n)
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s
def is_power_of_two(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0
def factorial(n):
    if n < 0:
        raise ValueError("Факторіал не визначений для від'ємних чисел")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def sum_of_digits(n):
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
