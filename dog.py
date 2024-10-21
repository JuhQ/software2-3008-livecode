import random

class Dog:
    created = 0

    # constructor, or initializer
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.age = 0
        self.legs = 4
        Dog.created = Dog.created + 1

    # useful in print statements
    def __str__(self):
        #return dir(self)
        return f"{self.age}, {self.breed}, {self.age}, {self.legs}"

    # our custom methods
    def get_legs(self):
        return self.legs

    def set_legs(self, legs):
        self.legs = legs

    def accident(self, count = 1):
        new_leg_count = self.legs - count
        if new_leg_count >= 0:
            self.set_legs(new_leg_count)

    def get_breed(self):
        return self.breed

    def set_breed(self, breed):
        self.breed = breed


Dog.outside_static_variable = True

dog = Dog("Juha", "Teacher")
dog.age = 12.32872346842376234876342
print(f"How many legs? {dog.get_legs()}")
dog.accident(1)
print(f"How many legs? {dog.get_legs()}")
dog.accident()
print(f"How many legs? {dog.get_legs()}")
dog.accident(-2)
print(f"How many legs? {dog.get_legs()}")
dog.accident(1)
print(f"How many legs? {dog.get_legs()}")
dog.accident(-20)
print(f"How many legs? {dog.get_legs()}")

print(f"Dog name: {dog.name:^10s}, breed: {dog.breed}, age: {dog.age:2.2f}")

dog2 = Dog("Musti", "Dogtor")
print(f"Dog name: {dog2.name}, breed: {dog2.breed}, age: {dog2.age}")

dog3 = Dog("Nuggets", "Labrador")
print(f"Dog name: {dog3.name}, breed: {dog3.breed}, age: {dog3.age}")

really_bad_kennel = [dog, dog2, dog3]

for i in range(10_000):
    """
    # dynamic variable definition (do not use)
    globals()['dog%s' % i] = Dog(f"dog {i}", "jep")
    """
    dog = Dog(f"dog {i}", "jep")
    really_bad_kennel.append(dog)

"""
dog6.accident(-100)
print(dog6.legs)
"""


really_bad_kennel[9].set_breed("Lhasa Apso")

for dog in really_bad_kennel:
    dog.accident(random.randint(0,4))
    print(f"{dog.name} ({dog.breed}) is in kennel, legs: {dog.legs}")


print(vars(dog))

print(dog2)
print(really_bad_kennel[9])

really_bad_kennel[9].accident()
print(really_bad_kennel[9])

print(vars(really_bad_kennel[9]))

# redefine static class parameter outside the class definition
# Dog.created = -1

print("How many dogs was created?")
print(Dog.created)

print("Can we create static class parameter outside of the class definition?")
print(Dog.outside_static_variable)
