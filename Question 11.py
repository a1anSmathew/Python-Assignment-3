class FormulaError(Exception):
    pass

def calculator():
    while True:
        user_input = input("Enter a formula (e.g. 1 + 1), or 'quit' to exit: ")

        if user_input.lower() == 'quit':
            print("Exiting the calculator. Goodbye!")
            break

        parts = user_input.split()

        try:
            # Check if the input has exactly 3 elements
            if len(parts) != 3:
                raise FormulaError("Formula must consist of two numbers and one operator.")

            num1 = float(parts[0])
            num2 = float(parts[2])

            operator = parts[1]
            if operator not in ('+', '-'):
                raise FormulaError("Invalid operator. Only '+' and '-' are allowed.")

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2

            print(f"The result of {num1} {operator} {num2} is: {result}")

        except ValueError:
            raise FormulaError("Both numbers must be valid numeric values.")

        except FormulaError as fe:
            print(f"FormulaError: {fe}")

calculator()