import random


def findout():
    value1 = random.randint(1, 10)
    value2 = random.randint(1, 10)

    answer = input('What is {0} + {1}: '.format(value1, value2))
    result = value1 + value2

    if answer == result:
        print('Your answer is correct')
    else:
        print('Your answer is incorrect')


if '__name__' == '__main__':
    findout()