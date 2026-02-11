class Student:
    def __init__(self,name,marks):
        self.name=name
        self._marks=marks
    def display(self):
        return self._marks
s=Student("Amaan",90)
print(s.display())
