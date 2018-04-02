people = ['joel', 'eli', 'tanya', 'gwyn']


def say_names(*args):
    for i in args:
        yield i


for i in say_names(*people):
    print(i)
