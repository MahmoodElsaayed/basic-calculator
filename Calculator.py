import re

class Calculator: 
    @classmethod
    def expression_validator(cls):
        while True:
            arithmetic_expression = input("Arithmetic expression: ").strip()
            if matches:= re.search(r"^(-?\d*.?\d+) *([-+*/]{1}) *(-?\d*.?\d+)$", arithmetic_expression):
                try:
                    return cls(float(matches.group(1)), float(matches.group(3)), matches.group(2))
                except ValueError:
                    pass
            print(f"'{arithmetic_expression}' is an Invalid arithmetic expression")
    
    def __init__(self, x, y, operator):
        self.x = x
        self.y = y
        self.operator = operator
        self.answer = self.calculate_answer()

    def calculate_answer(self):
        if self.operator == "+":
            return self.x + self.y
        elif self.operator == "-":
            return self.x - self.y
        elif self.operator == "*":
            return self.x * self.y
        elif self.operator == "/":
            if self.y == 0:
                raise ZeroDivisionError("Can't logically divide by zero")
            return self.x / self.y
        
    def __str__(self):
        return F"= {self.answer}"
    
def main():
    calculator = Calculator.expression_validator()
    print(calculator)

if __name__ == "__main__":
    main()

