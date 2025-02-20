numbers = list(range(1, 11))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print("Even:", even_numbers)
print("Odd:", odd_numbers)
