class Robot:

    def __init__(self, model):
        self.model = model
        
    def operate(self):
        print(f'\nМодель: {self.model}')


class CleanerRobot(Robot):

    def __init__(self, model):
        super().__init__(model)
        self.bag = 0

    def operate(self):
        self.bag += 1
        print(f'Пылесосим (+1) Мешок заполен на {self.bag}')


class WarRobot(Robot):

    def __init__(self, model, weapon):
        super().__init__(model)
        self.weapon = weapon

    def operate(self):
        print(f'Защищаю с помощью {self.weapon}')


class SubmarineRobot(WarRobot):

    def __init__(self, model, weapon, depth):
        super().__init__(model, weapon)
        self.depth = depth

    def operate(self):
        super().operate()
        print(f'Охрана ведется под водой на глубине {self.depth}')


cleaner = CleanerRobot('XIOMI-S1')
war = WarRobot('KX-15', 'gun')
submarine = SubmarineRobot('CV-22', 'canon', 1000)

cleaner.operate()
war.operate()
submarine.operate()
