import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time  
        print(f"{func.__name__} executed in: {execution_time:.4f} seconds")
        return result
    return wrapper

# Sample function to demonstrate the decorator
@measure_time
def sample_function():
    time.sleep(2)  # Simulate a function that takes time by sleeping for 2 seconds
    return "Function completed"

# Call the sample function
sample_function()