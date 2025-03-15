import time


def time_decorator(func):
    # Decorator function to measure runtime
    def wrapper(*args, **kwargs):
        start = time.time()
        # Record the start time

        result = func(*args, **kwargs)
        # Execute(실행) the original function
        # and save the result of the original function

        end_time = time.time()
        #Record the end time

        print(f"{func.__name__} took {end_time - start} seconds")
        return result
    return wrapper

