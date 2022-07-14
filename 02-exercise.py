# Given the below class:
class Cat:
    species: str = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('cat 1', 1)
cat2 = Cat('cat 2', 2)
cat3 = Cat('cat 3', 3)


# 2 Create a function that finds the oldest cat
def find_oldest_cat(*args):
    return max(args, key=lambda x: x.age)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is {find_oldest_cat(cat1, cat2, cat3).age} years old.')