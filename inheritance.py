class Thing():
    def __init__(self, **kwargs):
        if 'type' in kwargs: self._type = kwargs['type']
        if 'name' in kwargs: self._name = kwargs['name']


    def type(self, t=None):
        if t: self._type = t
        try: return self._type
        except AttributeError: return None

    def name(self, n=None):
        if n: self._name = n
        try: return self._name
        except AttributeError: return None

    def __str__(self):
        return f'I am a {self.type()} and my name is {self.name()}'


class Rock(Thing):
    def __init__(self, **kwargs):
        self._type = 'Rock'
        if 'type' in kwargs: del kwargs['type']
        super().__init__(**kwargs)


k = Rock(name='Amethyst')
print(k)
