how_high = int(input('Give me a two digit integer, please:')
count = 1
    while count <= how_high:
        if count %3 == 0 and count %5 == 0:
            print('FizzBuzz')
        count=count+1   
        if count %3 == 0 and count %5 != 0:
            print ('Fizz')
        count=count+1
        if count %3 != 0 and count %5 == 0:
            print ('Buzz')
        count=count+1
        else
            print (count)
