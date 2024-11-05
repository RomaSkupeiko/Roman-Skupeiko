year = 2024
word = 'Study'
it = 'Programming'
logical_type = True
key = {'min': 12, 'max': 6}

first_list = [year, word, it, logical_type, key]
print(first_list)

type_list = [type(year), type(word), type(it), type(logical_type), type(key)]
print(type_list)

int_type = 0
str_type = 0
bool_type = 0
dict_type = 0

for check in type_list:

    if check == int:
        int_type += 1

    elif check == str:
        str_type += 1

    elif check == bool:
        bool_type += 1

    elif check == dict:
        dict_type += 1

greatest_value = max(int_type, str_type, bool_type, dict_type)

if greatest_value == int_type:
    result = 'int'

elif greatest_value == str_type:
    result = 'str'

elif greatest_value == bool_type:
    result = 'bool'

elif greatest_value == dict_type:
    result = 'dict'

print("Найчастіший тип: ", result)