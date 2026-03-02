def is_power_of_two(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0
from utils import factorial

if __name__ == "__main__":
    number = 5
    print(f"Факторіал числа {number} дорівнює {factorial(number)}")
from utils import sum_digits
