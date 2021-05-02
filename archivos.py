def read():
    numbers = []
    with open('./archivos/numbers.txt', 'r', encoding = 'utf-8') as f:
        for line in f:
            if line.isspace() or line.isalpha():
                continue
            numbers.append(int(line))
    print(numbers)


def write():
    names = ['Pepe', 'Marcela', 'Fredy', 'Juan', 'Ana', 'Mara']
    with open('./archivos/names.txt', 'a', encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')

def run():
    read()
    write()


if __name__ == '__main__':
    run()