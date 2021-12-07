def Erasing(func):
    def check(ls):
        ls=list(filter(lambda x: x % 2 != 0, ls))
        return func(ls)
    return check


@Erasing
def func(ls):
    print(ls)


def main():
    ls=[10,15,13,54,105,208,307,405]
    func(ls)
if __name__=='__main__':
    main()