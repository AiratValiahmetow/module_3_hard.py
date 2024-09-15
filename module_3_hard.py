def calculate_structure_sum(data_structure):
    summa = 0
    flag_dict = 0
    flag_list = 0
    flag_int_float = 0
    flag_str = 0
    if isinstance(data_structure, dict):

        for key, value in data_structure.items():
            summa += calculate_structure_sum(key)
            summa += calculate_structure_sum(value)
            flag_dict += 1

    elif isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            summa += calculate_structure_sum(item)
        flag_list += 1

    elif isinstance(data_structure, (int, float)):
        summa += data_structure
        flag_int_float += 1

    elif isinstance(data_structure, str):
        summa += len(data_structure)
        flag_str += 1

    return summa






data_structure = [[1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),"Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print(result)