# class Car:
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.model = model
    
#     def full_name(self):
#         return f"your are is {self.__brand} {self.model} model"
    
#     def get_brand(self):
#         return f"{self.__brand} is great"

# my_car = Car("Tata", "2025")

# print(my_car.brand)
# print(my_car.get_brand())
# print(my_car.full_name())

# inhiret

class Animal:
    def __init__(self, name, voice):
        self.name = name
        self.voice = voice

    def full_expl(self):
        return f"this is a {self.name} it voice is {self.voice}"


first = Animal("Dog", "bhow bhow")

# print(first.full_expl())

class Cat(Animal):

    def __init__(self, name, voice, speed):
        self.speed = speed
        super().__init__(name, voice)

my_cat = Cat("bigi", "meiw", "20km/h")

# print(my_cat.name)
print(my_cat.full_expl())