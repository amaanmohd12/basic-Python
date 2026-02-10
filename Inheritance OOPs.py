class Animal:
    def speak(self):
        print("Animals make sounds")
class Dog(Animal):
    def barks(self):
        print("Dog barks!")

d=Dog()
d.speak()
d.barks()
