def do_logging(f):
    def wrapper():
        print('I was called before the function')
        f()
        print('I was called after the function')

    return wrapper

@do_logging
def say_my_name():
    print('My name is unknown')


say_my_name()