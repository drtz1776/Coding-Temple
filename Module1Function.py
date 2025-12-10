def create_list():
    list1 = []
    lengthInput = int(input('How many values with be in the list: '))
    for i in range(1, lengthInput + 1):
        list1.append(i)
    print(list1)

create_list()