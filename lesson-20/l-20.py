class Dog:
    def __init__(self, name: str) -> None:
        self.name = name

    def bark(self):
        print('Woof!')


class Chihuahua(Dog):
    pass


little_dog = Chihuahua('Pimpy')

print(little_dog.name)

little_dog.bark()
