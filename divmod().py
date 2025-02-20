num = int(input("Enter a number: "))
quotient, remainder = divmod(num, 2)
if remainder == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")
