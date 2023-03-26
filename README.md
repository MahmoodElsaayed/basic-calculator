# basic-calculator

a Python program that allows the user to input an arithmetic expression in the form of two operands and an operator, and returns the result of the expression. The program uses regular expressions to validate the user input before performing the calculation.

Here's how the program works:

1. The program imports re module.

2. The program defines a Calculator class.

3. The expression_validator method is a class method that validates the arithmetic expression input by the user. It uses a regular expression to check if the input matches the pattern of two operands and an operator. If the input is valid, the method returns a new instance of the Calculator class with the operands and operator as arguments.

4. The __init__ method initializes the x, y, and operator attributes of the Calculator instance. It then calls the calculate_answer method to calculate the answer attribute.

5. The calculate_answer method calculates the result of the arithmetic expression based on the operator attribute. If the operator is division and the second operand is 0, it raises a ZeroDivisionError.

6. The __str__ method returns the answer attribute of the Calculator instance.

7. The main function creates an instance of the Calculator class using the expression_validator class method. It then prints the answer using the __str__ method of the Calculator instance.

8. The if __name__ == "__main__": block checks if the program is being run as the main program, and if so, calls the main function.
Overall, the program provides a simple calculator functionality with basic error handling.
