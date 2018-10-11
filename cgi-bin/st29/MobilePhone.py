class MobilePhone:

    def __init__(self):
        self.set_data()
        
    def set_data(self):
        self.brand = input("Введите марку телефона:")
        self.screen_size = input("Введите размер экрана:")

    def display_data(self):
        print(self.brand, self.screen_size)
    
        
