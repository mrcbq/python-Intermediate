def run():
    # print(list(map(lambda x: x**2, range(1,101))), '\n')
    #Lista comprenhension, crear lista de los cuadrados de  los primeros 100 numbers solo si no son divisibles por 3
    # squares = [x**2 for x in range(1, 101) if x%3 != 0]

    # Reto: Crear una lista de todos los multiplos de 4, que sean multiplos de 6 y 9 hasta 5 digitos

    multiples = [x for x in range (1, 100000) if x % 4 == 0 and x % 6 == 0 and x % 9 == 0]

    # for x in range(1, 101):
    #     if x%3 != 0:
    #         squares.append(x**2)

    # print(squares)
    print(multiples)

if __name__ == '__main__':
    run()
