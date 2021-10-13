class Person:
    arms_count = 2

    def __init__(self):
        self.name = name

    def __str__(self):
        return f'Person<name={self.name}>'
    def greet(self):
        print(f'Hi {self.name}!')

    def __eq__(self, other):

me = Person('Nick')
clone = Person('Vasya')
you = Person('Vasya')


print(me, you)
print(me == clone)
me.greet()
you.greet()