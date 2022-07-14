# Inheritance
# Inheritance is a way to create new classes based on existing classes.

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def sign_in(self):
        return f'{self.username} has logged in'


class Character(User):
    def __init__(self, username: str, password: str, specialization: str, power: str):
        super().__init__(username, password)
        self.specialization = specialization
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


wizard = Character('joe', '123', 'wizard', 'fireball')
print(wizard.sign_in())
print(wizard .attack())
