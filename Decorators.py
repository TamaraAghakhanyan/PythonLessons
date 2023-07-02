#Decorator -    a function that takes on function as a parameter and
#               extends its functionality and behavior without modifying it.

def my_decorator(target_function):
    def function_wrapper():
        return "Python is such a " + target_function() + " language!"
    return function_wrapper

@my_decorator
def target_function():
    return "cool"

target_function()
