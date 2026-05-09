class SimpleLogger:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        print("Before function")
        result = self.function(*args, **kwargs)
        print("After function")
        return result


@SimpleLogger
def say_hello(name):
    print(f"Hello {name}")


say_hello("Daria")