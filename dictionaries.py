animals = dict(dog='woof', cat='meow')

people = {'mum': 'Tanya', 'dad': 'Gwyn'}

print(animals.keys())

print(people.values())

print('dog' in animals)

# Use get() to avoid exceptions if key doesn't exist
print(animals.get('dog'))