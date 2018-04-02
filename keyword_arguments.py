foods = dict(spinach='whole', potato='whole', chocolate='processed')


# kwargs is a convention
def food_chooser(**kwargs):
    if len(kwargs):
        for s in kwargs:
            print(f'{s} is a {kwargs[s]} food')


# Note that you pass the dict prefixed with **
food_chooser(**foods)
