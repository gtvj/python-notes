def expects_two(*args):
    numargs = len(args)

    if numargs != 2:
        raise TypeError(f'Expected two arguments but got {numargs}')

try:
    expects_two(1)

except TypeError as e:
    print(f'The error was: {e}')