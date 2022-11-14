def multiplication_table(number):
    sequence =""
    for x in range(1, 13):
        sequence += str(number * x) + " "
    print(sequence)

multiplication_table(8)

