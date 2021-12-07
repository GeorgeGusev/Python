def main():
    ls=(lambda **kwargs: {key * 2: value for key, value in kwargs.items()})(abc=3, abcd=4, abcde=5, abcdef=6)
    print(ls)

if __name__== '__main__':
    main()