def flatten(nested_list):
    flatten_list = []
    for i in nested_list:
        if isinstance(i, list):
            flatten_list.extend(flatten(i))
        else:
            flatten_list.append(i)
    return flatten_list

input_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten(input_list))