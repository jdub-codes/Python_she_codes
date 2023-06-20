class Dog:
    # state/attributes
    # name = "Jett"
    # age = 4
    # breed = "pug"

    # def __init__(self):
    #     pass

    # def __init__(self):
    #     self.name = "Jett"
    #     self.age = 4
    #     self.breed = "pug"

    
    def __init__(self, dog_name, dog_age, dog_breed):
        self.name = dog_name
        self.age = dog_age
        self.breed = dog_breed

    # methods/behaviours
    def eat(self): # any argument you're building should take the argument self
        print("Nom nom")

    def talk(self):
        print("Bark bark")

# dog1 = Dog() # instatiate
# dog1.talk() # no self argument during calling
# # print(dog1)

dog1 = Dog("Jett", 4, "pug")
dog2 = Dog("Ninja", 13, "dutch-sherpard")
print(dog2.age)
dog1.talk()

# the first letter of a class must be uppercase and what's underneath must be indented
# we have created an object from a class we defined
# when we define the class it becomes a template