verbs = ['run', 'love', 'sit']


def shout(*args):
    for s in args:
        print(s)


# Cant take any number of arguments
shout('shout', 'shout', 'let', 'it', 'all', 'out')

# There's a spread operator equivalent
shout(*verbs)


