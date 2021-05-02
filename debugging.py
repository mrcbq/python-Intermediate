def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    try:
        num = int(input('Put a number: '))
        if num < 0:
            raise ValueError('Sorry, no numbers below zero')
        print(divisors(num))
        print('The program ends')
    except ValueError:
        print('The input must be a number')



if __name__ == '__main__':
    run()