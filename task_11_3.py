class car:
    def __init__(self, marka, model, date, speed):
        self.__marka = marka
        self.__model = model
        self.__date = date
        self.__speed = speed

    @property
    def marka(self):
        return self.__speed

    @marka.setter
    def marka(self, speed):
        self.__speed = speed

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    def increase_speed_up(self):
        self.speed += 5

    def increase_speed_down(self):
        self.speed -= 5

    def print(self):
        print(self.__marka)
        print(self.__model)
        print(self.__date)
        print(self.__speed)

    def stop(self):
        self.speed = 0

    def turn_around(self):
        self.speed = -self.speed

class sport_car(car):
    def increase_speed_up(self):
        self.speed += 10

    def increase_speed_down(self):
        self.speed -= 10

class tractor(car):
    def check(self):
        if self.speed > 60:
            print(f'Внимание! Ваша скорость {self.speed}, максимально допустимая скорость движения 60 км/ч.')

    def increase_speed_down(self, k):
        self.speed -= k

    def increase_speed_up(self):
        if self.speed > 60:
            print('Необходимо снизить скорость до 60км/ч!')
            k = self.speed - 60
            self.increase_speed_down(k)
        else:
            self.speed += 5


class el_car(car):
    def __init__(self, marka, model, date, speed, battery):
        self.__marka = marka
        self.__model = model
        self.__date = date
        self.__speed = speed
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, battery):
        self.__battery = battery

    def level_of_battery(self):
        print(self.__battery)
        if self.__battery < 30:
            self.__speed = 20

    def print(self):
        print(self.__marka)
        print(self.__model)
        print(self.__date)
        print(self.__speed)
        print(self.__battery)

    def Power(self):
        self.__battery = 100


def main():
    car_test = sport_car('SUBARU', 'WRX STI', '01.2020', 150)
    car_test.print()
    print(' ')
    car_test.increase_speed_up()
    car_test.print()
    print(' ')
    car1 = tractor('Belarus', "МТЗ-510", "02.2000", 80)
    car1.print()
    car1.check()
    car1.increase_speed_up()
    print(' ')
    car1.print()
    print(' ')
    car2 = el_car('Chevrolet', 'Volt', '10.2017', 100, 55)
    car2.print()
    print(' ')
    car2.level_of_battery()
    print(' ')
    car2.print()
    print(' ')
    car2.Power()
    car2.print()


if __name__ == '__main__':
    main()