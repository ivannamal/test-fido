def evaluate(my_list):
    n = len(my_list)
    desired_pos = int(((2 * n) / 3) - 1)
    if n <= 1:
        return None
    desired_element = my_list[desired_pos]
    return desired_element


print(evaluate([0, 1, 2, 3, 4]))
print(evaluate([1, 2, 3]))
