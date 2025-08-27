def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    # Assume the first element is the largest
    max_val = my_list[0]

    # Compare with the rest
    for num in my_list[1:]:
        if num > max_val:
            max_val = num

    return max_val
