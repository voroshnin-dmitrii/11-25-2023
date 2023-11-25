class Man:
    __count = 0

    def __init__(self, name, age):
        self.__name = ''
        self.__age = 0
        self.set_name(name)
        self.set_age(age)

        self.__count += 1

    def set_name(self, name):
        if name.isalpha():
            self.__name = name
        else:
            raise ValueError('Ошибка в возрасте')

    def set_age(self, age):
        if 0 <= age <= 100:
            self.__age = age
        else:
            raise ValueError('Ошибка в возрасте')

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


new_man = Man('M0x', 35)

