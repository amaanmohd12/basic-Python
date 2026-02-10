class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def display(self):
        print(f"The students details are:{self.name}{self.roll_no}")
s1=Student("Amaan",10)
s2=Student("Muaaz",23)
s1.display()
s2.display()
