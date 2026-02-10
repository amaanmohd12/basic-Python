class Car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def start(self):
        print(f"{self.color}{self.brand}is starting...")
car1=Car("Tesla","Red")
car2=Car("BMW","Black")

car1.start()
car2.start()
