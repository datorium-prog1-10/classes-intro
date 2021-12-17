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

    def freeze(self, target):
        if self.energy >= 150:        
            target.frozen = True
            print(f"{self.name} has frozen {target.name}!")
            self.energy -= 150
        else:
            print(f"Not enough energy!")

    def restore(self, target):
        target.frozen = False
        print(f"{self.name} has restored {target.name}!")


human = Creature("Anna", 15, 0)
skolens = Creature("Miks", 16, 0)
skolens2 = Creature("Jenifer", 14, 0)
wizard = Creature("Gandalf", 24000, 1000)
witch = Creature("Medusa", 400, 200)
witch2 = Creature("Darker", 600, 200)

human.introduce()
wizard.introduce()
witch.introduce()
human.check_energy()
witch.check_energy()

human.jump(5)
wizard.jump(20)

witch.freeze(human)
witch.check_energy()

skolens.restore(human)
human.jump(2)