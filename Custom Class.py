class Number:
    def __init__(self, value):
        self.value = value
    
    def check_even_odd(self):
        return "Even" if self.value % 2 == 0 else "Odd"

num = Number(int(input("Enter a number: ")))
print(f"{num.value} is {num.check_even_odd()}")
