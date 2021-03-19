def swapFile():
    a = input(" Enter the name of File 1: ")
    b = input(" Enter the name of File 2: ")
    print(a)
    print(b)
    # open1 = open(a)
    # data_a = open1.read()
    # open2 = open(b)
    # data_b = open2.read()
    with open(a, "r") as file1:
        data_a = file1.read()
    with open(b, "r") as file2:
        data_b = file2.read()

    with open(a, "w") as file1:
        file1.write(data_b)
    with open(b, "w") as file2:
        file2.write(data_a)
swapFile()
