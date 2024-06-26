class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

def get_number():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    return a, b

def main():
    a, b = get_number()
    calc = Calculator(a, b)
    print(f"Addition: {calc.add()}")
    print(f"Subtraction: {calc.sub()}")
    print(f"Multiplication: {calc.mul()}")
    print(f"Division: {calc.div()}")

if __name__ == "__main__":
    main()
