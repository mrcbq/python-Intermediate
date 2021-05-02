def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    num = input('Put a number: ')
    assert num.isnumeric(), 'You must be enter a integer number greater than zero'
    print(divisors(int(num)))


if __name__ == '__main__':
    run()