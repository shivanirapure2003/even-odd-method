import numpy as np

numbers = np.array(range(1, 11))
even_numbers = numbers[numbers % 2 == 0]
odd_numbers = numbers[numbers % 2 != 0]

print("Even:", even_numbers)
print("Odd:", odd_numbers)
