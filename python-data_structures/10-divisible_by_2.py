def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    max_val = my_list[0]   # start with the first element
    i = 1
    while i < len(my_list):
        if my_list[i] > max_val:
            max_val = my_list[i]
        i += 1
    return max_val
