from Class_Pets import Pet

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet, pet_type):
        self.first_name = first_name
        self.treats = treats
        self.pet_food = pet_food
        self.last_name = last_name
        self.pet = pet
        self.pet_type = pet_type

        self.p = Pet(self.pet, pet_type, 'handshake')
    def walk(self):
        self.p.play()
        print(f'You walked your {self.pet_type} they now have {self.p.health} Health')
    def feed(self):
        self.p.eat()
        print(f'You fed {self.pet_type}, they now have {self.p.health} Health and {self.p.energy} Energy')
    def bathe(self):
        self.p.noise()
        print('You struggle...')
        self.p.noise()

