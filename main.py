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
import utils

test_val = 125
if utils.is_power_of_five(test_val):
    print(f"Число {test_val} є степенем 5")
else:
    print(f"Число {test_val} не є степенем 5")

numbers_to_check = [1, 5, 20, 25, 100]
print("\n--- Перевірка списку чисел на степінь 5 ---")
for n in numbers_to_check:
    print(f"{n}: {utils.is_power_of_five(n)}")
