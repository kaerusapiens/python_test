def decorator_A(func):
    def wrapper():
        print("decorator_A: Before calling", func.__name__)
        func()
        print("decorator_A: After calling", func.__name__)
    return wrapper

def decorator_B(func):
    def wrapper():
        print("decorator_B: Before calling", func.__name__)
        func()
        print("decorator_B: After calling", func.__name__)
    return wrapper

@decorator_A
@decorator_B
def hello():
    print("Hello, World!")
hello()

print()
@decorator_B
@decorator_A
def hello():
    print("Hello, World!")

hello()
"""
decorator_A: Before calling wrapper
decorator_B: Before calling hello
Hello, World!
decorator_B: After calling hello
decorator_A: After calling wrapper

decorator_B: Before calling wrapper
decorator_A: Before calling hello
Hello, World!
decorator_A: After calling hello
decorator_B: After calling wrapper
"""