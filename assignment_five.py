import random
'''this program is about guess a number, the user need to enter the number and take a guess'''
def get_random():
    number = random.randint(1, 100)
    print('Well, '', I am thinking of a number between 1 and 100.')
    return number

def getguess():
    print('Take a guess.')
    guess = input()
    return guess


def main():
    randomnumbers = int(get_random())

    while True:

        getguessnumbers = int(getguess())
        if randomnumbers < getguessnumbers:
            print("your number is too high")

        if randomnumbers > getguessnumbers:
            print("your number is too low")

        if randomnumbers == getguessnumbers:
            print("the number is correct")
            break


main()
    





