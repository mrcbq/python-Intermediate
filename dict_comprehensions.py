def run():
    # my_dict = {}

    # for i in range(1,101):
    #     if i % 3 !=0:
    #         my_dict[i] = i**3

    my_dict = {x: round(x**0.5, 2) for x in range(1,1001)}

    print(my_dict)



if __name__ == '__main__':
    run()
