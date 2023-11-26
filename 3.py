class Ship:

    def __init__(self, model):
        self.model = model

    def __str__(self):
        return f'Модель: {self.model}'

    @staticmethod
    def sail():
        print('Плывем!')


class CargoShip(Ship):

    def __init__(self, model):
        super().__init__(model)
        self.tonnage = 0

    def load(self):
        self.tonnage += 1
        print(f'Погрузка (+1). Текущая загруженность: {self.tonnage}')

    def unload(self):
        if self.tonnage > 0:
            self.tonnage -= 1
        print(f'Разгрузка (-1). Текущая загруженность: {self.tonnage}')


class WarShip(Ship):

    def __init__(self, model, weapon):
        super().__init__(model)
        self.weapon = weapon

    def attack(self):
        print(f'Атакую с помощью {self.weapon}')


cargo = CargoShip('Susanin')
print(cargo)
for _ in range(2):
    cargo.load()
cargo.sail()
cargo.unload()

warship = WarShip('TTX-15', 'gun')
print(warship)
warship.sail()
warship.attack()



