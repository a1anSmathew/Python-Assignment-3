def division(num1, num2):
    try:
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Invalid input. Please provide numbers.")
    except Exception as e:
        print(f"An unknown error occurred: {e}")
    finally:
        print("Execution completed. Thank you for using the division function.")

division(10, 0)
division(10, 'a')
division(10, 2)