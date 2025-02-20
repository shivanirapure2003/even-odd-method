def check_even_odd(n):
    if n == 0:
        return "Even"
    elif n == 1:
        return "Odd"
    else:
        return check_even_odd(n - 2)

num = int(input("Enter a number: "))
print(f"{num} is {check_even_odd(num)}")
