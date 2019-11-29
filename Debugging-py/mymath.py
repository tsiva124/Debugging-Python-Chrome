import brainteaser
import random
info = True


def findout():
    value1 = random.randint(1, 10)
    value2 = random.randint(1, 10)
    answer = input('What is {0} + {1}: '.format(value1, value2))
    result = value1 + value2

    if answer == result:
        print('Your answer is correct')
    else:
        print('Your answer is incorrect')

def add(x, y):
    """
    Add two numbers
    :param x:
    :param y:
    :return:
    """
    return x+y


def main():
    num1 = 10
    num2 = 20
    result = add(num1, num2)
    num2 = 30
    print(result)


if __name__ == '__main__':
    findout()