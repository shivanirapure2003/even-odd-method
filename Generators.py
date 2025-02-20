def even_numbers(lst):
    return (num for num in lst if num % 2 == 0)

def odd_numbers(lst):
    return (num for num in lst if num % 2 != 0)

numbers = range(1, 11)
print("Even:", list(even_numbers(numbers)))
print("Odd:", list(odd_numbers(numbers)))
