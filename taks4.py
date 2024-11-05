def dublicate(dubli_list):
    num = []
    
    for check in dubli_list:
        if check not in num:
            num.append(check)
    return num


def sort_list(so_list):
    num1 = []
    strr2 = []

    for check in so_list:
        if type(check) == int:
            type(check) == float
            num1.append(check)

        elif type(check) == str:
            strr2.append(check)

    num1.sort()
    strr2.sort(key=str.lower)
    return num1, strr2


dubli_list = [3, 1, 2, 3, 4, 5, 6, 3, 4, 5, 7,
              6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'анаконда']
listt = dubli_list
first_list = dublicate(dubli_list)
second_list = sort_list(first_list)
print(f'Невідсортований список: {
      listt}\nВідсортований список: {second_list} ')