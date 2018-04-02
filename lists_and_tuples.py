def main():
    # A list
    game_list = ['rock', 'paper', 'scissors', 'car', 'water', 'lemon', 'moss']

    # A tuple
    name_tuple = ('rock', 'sock', 1, {'name': 'foo'}, 'scissors', 'car', 'water', 'lemon', 'moss')

    # Slice
    print(name_tuple[3:7])

    # Slice with increment
    print(name_tuple[1:6:2])

    # Get index
    print(name_tuple.index('rock'))

    # Add item
    game_list.append('computer')

    # Add prepend
    game_list.insert(0, 'fish')

    # Remove by value
    game_list.remove('water')

    # Remove and return last item (can also pass an index)
    last_item = game_list.pop()

    # Delete an item by index
    del game_list[3]

    # Get the length
    print(len(game_list))

    print(', '.join(game_list))

    print_list(game_list)


def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()


if __name__ == '__main__': main()
