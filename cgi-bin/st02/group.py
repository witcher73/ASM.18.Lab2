import pickle

from .device import Device
from .smartphone import Smartphone


class Office:

    FILENAME = 'cgi-bin/st01/test'

    def __init__(self):
        self.devices = []

    def get_devices(self):
        return self.devices

    def add_device(self, vendor: str, model: str):
        b = Device(vendor, model)
        self.devices.append(b)


    def add_smartphone(self, vendor: str, model: str, os: str):
        m = Smartphone(vendor, model, os)
        self.devices.append(m)


    def print_list(self):
        if len(self.devices) == 0:
            print('Список пуст')
            return

        print('------------------------------')
        for p in self.devices:
            print('\t', p.__class__.__name__)
            p.display()
            print('------------------------------')


    def edit_list(self):
        if len(self.devices) == 0:
            print('Список пуст')
            return

        print('Количество устройств: ', len(self.devices))

        try:    
            ind = int(input('Для редактирования введите индекс (0 вернуться назад): '))

            if ind == 0:
                return

            self.devices[ind - 1].read_input()
        except Exception as ex:
            print(ex)
            print('Ошибка!')


    def save_to_file(self):
        try: 
            with open(self.FILENAME, 'wb') as f:
                pickle.dump(self.devices, f, -1)
        except Exception as ex:
            print(ex)
            print('Ошибка!')


    def load_from_file(self):
        try:
            with open(self.FILENAME, "rb") as f:
                self.devices = pickle.load(f)
        except FileNotFoundError:
            print('<script>alert("Нет файла")</script>')


    def delete_from_list(self, i: int):
        del self.devices[i]

    
    def clear(self):
        self.devices = []