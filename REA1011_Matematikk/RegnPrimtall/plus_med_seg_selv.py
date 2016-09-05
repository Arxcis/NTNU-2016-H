

# python adder

const_number = int(input("Type number: "));
number = const_number
g = ""
count = 0

while g != 'q':
    count += 1

    g = input(str(count) + ': ' + str(number))
    number += const_number