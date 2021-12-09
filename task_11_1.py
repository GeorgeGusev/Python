class mobile_phone:
    Model = 0
    Color = None
    Weight = 0

    def __init__(self, model, color, weight):
        self.__Model = model
        self.__Color = color
        self.__Weightt = weight

    @property
    def Model(self):
        return self.__Model

    @Model.setter
    def Model(self, model):
        self.__Model = model

    @property
    def Color(self):
        return self.__Color

    @Color.setter
    def Color(self, color):
        self.__Color = color

    @property
    def Weight(self):
        return self.__Weight

    @Weight.setter
    def Weight(self, weight):
        self.__Weight = weight

    def to_make(self):
        self.__Model -= 1



class car:
    Model = 0
    Color = None
    Year = None

    def __init__(self, model, color, Year):
        self.__Model = model
        self.__Color = color
        self.__Year = year

    @property
    def Model(self):
        return self.__Model

    @Model.setter
    def Model(self, model):
        self.__Model = model

    @property
    def Color(self):
        return self.__Color

    @Color.setter
    def Color(self, color):
        self.__Color = color

    @property
    def Year(self):
        return self.__Year

    @Year.setter
    def Year(self, year):
        self.__Year = year

    def drive(self, model):
        self.__Model = model



class Country:
    Сapital = None
    Mainland = None
    Сoordinates = None

    def __init__(self, capital, mainland, coordinates):
        self.__Сapital = capital
        self.__Mainland = mainland
        self.__Сoordinates = coordinates

    @property
    def Сapital(self):
        return self.__Сapital

    @Сapital.setter
    def Сapital(self, capital):
        self.__Сapital = capital

    @property
    def Mainland(self):
        return self.__Mainland

    @Mainland.setter
    def Mainland(self, mainland):
        self.__Mainland = mainland

    @property
    def Сoordinates(self):
        return self.__Сoordinates

    @Сoordinates.setter
    def Сoordinates(self, coordinates):
        self.__Сoordinates = coordinates

    def fly(self, coordinates):
        self.__Сoordinates = coordinates


class children:
    name = None
    birthday = 0
    sex = 0

    def __init__(self, name, birthday, sex):
        self.__Name = name
        self.__Birthday = birthday
        self.__Sex = sex

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, name):
        self.__name = name

    @property
    def Birthday(self):
        return self.__birthday

    @Birthday.setter
    def Height(self, birthday):
        self.__Birthday = birthday

    @property
    def Sex(self):
        return self.__sex

    @Sex.setter
    def Material(self, sex):
        self.__Sex = sex

    def new_name(self, name):
        self.__Name = name


class tire:
    size = 0
    brand = None
    max_speed = None

    def __init__(self, size, brand, max_speed):
        self.__size = size
        self.__Brand = brand
        self.__Max_speed = max_speed

    @property
    def Size(self):
        return self.__size

    @Size.setter
    def Size(self, size):
        self.__size = size

    @property
    def Brand(self):
        return self.__brand

    @Brand.setter
    def Color(self, brand):
        self.__Brand = brand

    @property
    def Max_speed(self):
        return self.__max_speed

    @Max_speed.setter
    def Max_speed(self, max_speed):
        self.__Max_speed = max_speed

    def go(self):
        print('Vrum-vrum')