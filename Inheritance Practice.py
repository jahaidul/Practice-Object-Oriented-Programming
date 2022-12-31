class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed
    
    def make_sound(self):
        print("Bark!")

fido = Dog("Fido", "Labrador")
print(fido.name)   # "Fido"
print(fido.species) # "Dog"
print(fido.breed)  # "Labrador"
fido.make_sound()  # "Bark!"
