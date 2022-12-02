def sequence(number):
    counter = 0
    while True:

        if number % 2 == 0:
            counter = counter + 1
            number = number / 2
            print (number)
            if number == 1:
                return counter



        if number % 2 == 1:
            counter = counter + 1
            number = number * 3 + 1
            print(number)
            if number == 1:
                return counter


def main():
    number = int(input("please enter the number "))
    print("it toke", sequence(number) ,"steps")





if __name__ == '__main__':
    main()

