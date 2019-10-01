high_number = input("Enter an integer:")
number = int(high_number)
count = 1

while count <= number:
    if count %3 == 0 and count %5 == 0:
        print('FizzBuzz for', count)
    if count %3 == 0 and count %5 != 0:
        print('Fizz for ', count)
    if count %3 != 0 and count %5 == 0:
        print('Buzz for ', count)
    else:
        print(count)
    count = count + 1
