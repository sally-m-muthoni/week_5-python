#ACTIVITY1
# Parent class
class Superhero:
    def __init__(self, name, alias, superpower, origin):
        self.name = name  # Public attribute
        self.alias = alias
        self.__origin = origin  # Private attribute
        self.superpower = superpower

    def introduce(self):
        print(f"I am {self.alias}, and my superpower is {self.superpower}!")

    def get_origin(self):  # Public method to access private attribute
        return self.__origin

# Child class
class Speedster(Superhero):
    def __init__(self, name, alias, superpower, origin, speed):
        super().__init__(name, alias, superpower, origin)
        self.speed = speed

    def show_speed(self):
        print(f"{self.alias} can run at {self.speed} mph!")

# Using the classes
hero1 = Superhero("Clark Kent", "Superman", "Super Strength", "Krypton")
hero1.introduce()
print(f"Origin: {hero1.get_origin()}")  # Access private attribute via a public method

flash = Speedster("Barry Allen", "The Flash", "Super Speed", "Central City", 299792)
flash.introduce()
flash.show_speed()


#ACTIVITY2
# Parent class
class Animal:
    def move(self):
        print("This animal moves.")

# Child classes with polymorphism
class Dog(Animal):
    def move(self):
        print("The dog runs on four legs. 🐕")

class Bird(Animal):
    def move(self):
        print("The bird flies in the sky. 🐦")

class Fish(Animal):
    def move(self):
        print("The fish swims in the water. 🐟")

# Using polymorphism
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    animal.move()  # Each class defines move() differently

# Parent class
class Vehicle:
    def move(self):
        print("This vehicle moves.")

# Child classes with polymorphism
class Car(Vehicle):
    def move(self):
        print("The car drives on roads. 🚗")

class Plane(Vehicle):
    def move(self):
        print("The plane flies in the sky. ✈️")

class Boat(Vehicle):
    def move(self):
        print("The boat sails on water. 🚢")

# Using polymorphism
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()  # Each class defines move() differently

