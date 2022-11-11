#Owen 10/11/2022
def count(first, last):
    test = ""
    for x in range(first, last):
        test += str(x)+" "
    print(test)



def main():
    count(0, 7)
    count(7, 0)






if __name__ == '__main__':
    main()
