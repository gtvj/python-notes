import sys


def main():
    try:
        x = x
    except ValueError:
        print('I encountered a value error')
    except ZeroDivisionError:
        print('You can\'t divide by zero')
    except:
        print(f'Unknown error: {sys.exc_info()}')
    else:
        print(f'All good, x is now {x}')


if __name__ == '__main__': main()
