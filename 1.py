class Point:

    def __init__(self, x=0, y=0):
        self.set_x(x)
        self.set_y(y)

    def __str__(self):
        return 'Point ({}:{})'.format(
            self.get_x(), self.get_y()
        )

    def set_x(self, x):
        if isinstance(x, int):
            self.__x = x
        else:
            raise Exception('Недопустимое значение')

    def set_y(self, y):
        if isinstance(y, int):
            self.__y = y
        else:
            self.__y = 0

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y


point = Point(x=5)
print(point)

