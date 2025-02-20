numbers = range(1, 11)
results = list(map(lambda x: (x, "Even" if x % 2 == 0 else "Odd"), numbers))
print(results)
