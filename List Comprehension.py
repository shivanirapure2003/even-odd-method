numbers = list(range(1, 11))
even_numbers = [x for x in numbers if x % 2 == 0]
odd_numbers = [x for x in numbers if x % 2 != 0]

print("Even:", even_numbers)
print("Odd:", odd_numbers)
