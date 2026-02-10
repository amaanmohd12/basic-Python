class Rectangle:
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def cal_area(self):
        area=self.breadth*self.length
        print("Area of the rectangle:",area)
r=Rectangle(41,2)
r.cal_area()
