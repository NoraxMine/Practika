class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
    
    def make_sound(self):
        print('*sound*')
    
    def info(self):
        print(self.name)
        print(self.age)
        print(self.species)

    def __del__(self):
        print('del done')

class Dog(Animal):
    def __init__(self, name, age, species, breed, guard_status):
        super().__init__(name, age, species)
        self.breed = breed
        self.guard_status = guard_status
    
    def info(self):
        super().info()
        print(self.breed)
        print(self.guard_status)
    
    def guard_house(self):
        super().make_sound()
