# An interator object is functionally equivalent
# to a generator object but
#  1. more complex to implement
#  2. does not use yield

class my_iterator:

    def __init__(self, stop=None):
        self._next = 0
        self._stop = stop if stop else 10

    # identifies object as iterator
    def __iter__(self):
        return self

    # constructs like 'for' loops look
    # for the __next__ function
    def __next__(self):
        if self._next >= self._stop:
            raise StopIteration
        else:
            self._next += 1
            return self._next


for n in my_iterator(40):
    print(n, end=' ')
