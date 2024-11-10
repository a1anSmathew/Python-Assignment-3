def log_function_call(func):

    def wrapper(*args, **kwargs):

        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")

        result = func(*args, **kwargs)

        print(f"{func.__name__} returned: {result}")

        return result

    return wrapper


# Apply the decorator to the add function
@log_function_call
def add(a, b):
    return a + b


# Example usage
add(2, 3)