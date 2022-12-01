def get_input():

    while True:
        number = input("please inter number 1, 2, 3 ,4, 5, 6, 7, 8, 9,10,")
        number = int(number)
        if number >= 1 and number <= 10:
                return number





def main():
    print("you entered", get_input())


if __name__ == '__main__':
    main()
