import utils

test_numbers = [8, 16, 17, 0]

for num in test_numbers:
    if utils.is_power_of_two(num):
        print(f"Число {num} є степенем двійки")
    else:
        print(f"Число {num} НЕ є степенем двійки")

from utils import factorial

if __name__ == "__main__":
    number = 5
    print(f"Факторіал числа {number} дорівнює {factorial(number)}")
