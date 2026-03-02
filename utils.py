def is_power_of_two(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0

def factorial(n):
    if n < 0:
        raise ValueError("Факторіал не визначений для від'ємних чисел")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
