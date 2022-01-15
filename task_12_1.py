class MyTime:
# Конструктор (ч:м:с)
    def __init__(self, hours=None, min=None, sec=None):
        if type(hours) == type(min) == type(sec) == int:
            self._hours = hours
            self._min = min
            self._sec = sec
        elif type(hours) == str:
            tmp = hours.split(":")
            self._hours = int(tmp[0])
            self._min = int(tmp[1])
            self._sec = int(tmp[2])
        elif isinstance(hours, MyTime):
            self._hours = hours._hours
            self._min = hours._min
            self._sec = hours._sec
        elif hours == min == sec is None:
            self._hours = 0
            self._sec = 0
            self._min = 0

# Методы:
    def Print(self):
        if self._sec > 60:
            k = self._sec % 60
            c = self._sec // 60
            self._sec = k
            self._min += c
        if self._min > 60:
            k = self._min % 60
            c = self._min // 60
            self._min = k
            self._hours += c
        if self._hours > 24:
            k = self._hours % 24
            c = self._hours // 24
            self._hours = k
        print(f"{self._hours}:{self._min}:{self._sec}")

    def __eq__(self, other):  # ==
        return self._hours == other._hours and self._min == other._min and self._sec == other._sec

    def __ne__(self, other):  # !=
        return self._hours != other._hours or self._min != other._min or self._sec != other._sec

    def __ge__(self, other):  # >=
        return ((self._hours * 60 + self._min) + self._sec / 60) >= (
                (other._hours * 60 + other._min) + other._sec / 60)

    def __le__(self, other):  # <=
        return ((self._hours * 60 + self._min) + self._sec / 60) <= (
                (other._hours * 60 + other._min) + other._sec / 60)

    def __gt__(self, other):  # >
        return ((self._hours * 60 + self._min) + self._sec / 60) > (
                (other._hours * 60 + other._min) + other._sec / 60)

    def __lt__(self, other):  # <
        return ((self._hours * 60 + self._min) + self._sec / 60) < (
                (other._hours * 60 + other._min) + other._sec / 60)

    def __add__(self, other):
        time = MyTime()
        time._hours = self._hours + other._hours
        time._minutes = self._min + other._min
        time._seconds = self._sec + other._sec
        time.Print()

    def __sub__(self, other):
        time = MyTime()
        time._hours = abs(self._hours - other._hours)
        time._minutes = abs(self._min - other._min)
        time._seconds = abs(self._sec - other._sec)
        time.Print()

    def __mul__(self, other):
        time = MyTime()
        time._hours = self._hours * other
        time._minutes = self._min * other
        time._seconds = self._sec * other
        time.Print()


def main():
    r = MyTime('12:65:83')
    s = MyTime(1, 15, 60)
    print(r == s)
    print(r != s)
    print(r >= s)
    print(r <= s)
    print(r > s)
    print(r < s)
    r + s
    r - s
    r * 1


if __name__ == '__main__':
    main()