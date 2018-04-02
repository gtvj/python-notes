class Earthling:
    # static member
    i_am_static = [1, 2, 3]

    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'not supplied'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'not supplied'
        self._movement = kwargs['movement'] if 'movement' in kwargs else 'not supplied'

    # These methods behave as both setters and getters
    def type(self, t=None):
        if t:
            self._type = t
        return self._type

    def move(self, m=None):
        if m:
            self._movement = m
        return self._movement

    def sound(self, s=None):
        if s:
            self._sound = s
        return self._sound

    # Specially named method that provides string representation of object
    def __str__(self):
        return f'I am a {self.type()} that will {self.sound()} as I {self.move()}'


def main():
    worm = Earthling(type='worm', movement='slip', sound='boing')
    worm.sound('yippeeeeee')
    print(worm)


if __name__ == '__main__': main()
