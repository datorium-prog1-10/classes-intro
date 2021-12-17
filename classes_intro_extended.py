class Creature:
    def __init__(self, name, age, energy, frozen = False):
        self.name = name
        self.age = age
        self.energy = energy
        self.frozen = frozen

    def introduce(self):
        print(f"Hey, my name is {self.name} and I am {self.age} years old.")

    def check_energy(self):
        print(f"{self.name} has {self.energy} energy.")
    
    def jump(self, distance):
        if not self.frozen:
            print(f"{self.name} jumps {distance} meters.")
        else:
            print(f"{self.name} is frozen!")

class Human(Creature):
    def calculate_sum(self, a, b):
        print(f"The sum is {a+b}")

class Witch(Creature):
    def freeze(self, target):
        if self.energy >= 150:        
            target.frozen = True
            print(f"{self.name} has frozen {target.name}!")
            self.energy -= 150
        else:
            print(f"Not enough energy!")

class Wizard(Creature):
    def restore(self, target):
        target.frozen = False
        print(f"{self.name} has restored {target.name}!")

skolens1 = Human("Anna", 14, 0)
skolens2 = Human("Jenifer", 15, 0)
enemy1 = Witch("Medusa", 400, 200)
enemy2 = Witch("Darker", 600, 200)
friend1 = Wizard("Gandalf", 24000, 1000)

enemy1.freeze(skolens1)
friend1.restore(skolens1)