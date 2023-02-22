def reverse_nums(nested_list):
    reverse_list = []
    for i in nested_list[::-1]:
        if isinstance(i, list):
            reverse_list.append(reverse_nums(i))
        else:
            reverse_list.append(i)
    return reverse_list

input_list = [[1, 2], [3, 4], [5, 6, 7]]
print(reverse_nums(input_list))
