class Rectangle :
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.__x1=x1
        self.__x2=x2
        self.__y1=y1
        self.__y2=y2

    def set(self, x1, x2, y1, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        
    def show(self):
        print(f"좌측 상단 꼭지점이 ({self.__x1}, {self.__y1})이고 우측 하단 꼭지점이 ({self.__x2}, {self.__y2})인 사각형입니다.")

    def getWidth(self):
        Width = self.__x2 - self.__x1
        return Width

    def getHeight(self):
        Height = self.__y2 - self.__y1
        return Height

    def getArea(self):
        Area = self.getHeight() * self.getWidth()
        return Area

    def getPerimeter(self):
        Perimeter = 2*self.getWidth() + 2*self.getHeight()
        return Perimeter

r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p= r1.getPerimeter()

r1.show()
print(f"\n넓이는 {a}, 둘레는 {p}")
