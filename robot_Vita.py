import os
import time


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            return cls._instances[cls]
        raise MoreThanOneRobotException


class Robot(metaclass=Singleton):
    def __init__(self):
        super().__init__()
        self._serial_number = 'АА001221-56'
        self._name = '-'
        self._place = '-'
        self._functionality = '-'

    def __str__(self):
        return f'Серийный номер: {self._serial_number}\n' + \
                f'Наименование: {self._name}\n' + \
                f'Место нахождения: {self._place}\n' + \
                f'Функциональность: {self._functionality}'


class RobotV(Robot):
    def __init__(self):
        super().__init__()
        self._name = 'B'
        self._place = 'Завод'


class RobotDecorator(Robot):
    def __init__(self, robot):
        super().__init__()
        self._robot = robot


class RobotVita(RobotDecorator):
    def __init__(self, robot):
        super().__init__(robot)
        self._name = 'Вита'
        self._place = '"ООО Кошмарик"'
        self._functionality = '"постройка домов"\n"постройка сараев"'


class RobotVitaliy(RobotDecorator):
    def __init__(self, robot):
        super().__init__(robot)
        self._name = 'Виталий'
        self._place = '"ООО Кошмарик"'
        self._functionality = robot._functionality + '\n"добавление этажей к постройке"\n"снос верхнего этажа у постройки"'


def print_loading(text: str):
    print(text, end='')
    print('')
    s = '|'
    for i in range(101):
        time.sleep(0.04)
        print('\r', 'Загрузка', i*s, str(i), '%', end='')
    print('\nЗагрузка завершена')


def print_info(header: str, robot: Robot):
    os.system('cls')
    print(header.capitalize() + '!\n')
    print(str(robot) + '\n')
    input('Нажмите enter для продолжения...')
    os.system('cls')


if __name__ == '__main__':
    print_loading('Создание робота')
    robotV = RobotV()
    print_info('Характеристики робота после создания:', robotV)

    print_loading('Первичное обучение')
    robotVita = RobotVita(robotV)
    print_info('Характеристики робота после первичного обучения:', robotVita)

    print_loading('Эксплуатация на предприятии')
    robotVitaliy = RobotVitaliy(robotVita)
    print_info('Характеристики робота после эксплуатации:', robotVitaliy)
