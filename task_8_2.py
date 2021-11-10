def palindrome(word: str):
    if len(word) == 1 or len(word) == 2:
        print(f'\'{word}\' - не  палиндромом!')
    elif word == word[::-1]:
        print(f'\'{word}\' - палиндромом!')
    else:
        print(f' \'{word}\' - не палиндромом!"')

def main():
    print('Введите 5 слов: ')
    count = 0
    tmp = []
    while count != 5:
        word = str(input())
        tmp.append(word)
        count += 1
    for i in tmp:
        palindrome(i)

if __name__ == '__main__':
    main()