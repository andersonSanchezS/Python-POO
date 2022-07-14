# OOP
class PlayerCharacter:

    def __init__(self, name: str = 'anonymous', age: int = 19):
        self.name = name
        self.age = age
    '''
    def shout(self):
        return f'My name is {self.name}'

    @classmethod
    def adding_numbers(cls, num1: int, num2: int):
        return num1 + num2

    @staticmethod
    def multiply_numbers(num1: int, num2: int):
        return num1 * num2

    def speak(self):
        return f"My name is {self.name} and i'm {self.age} years old"
    '''


player1 = PlayerCharacter('Tom')
