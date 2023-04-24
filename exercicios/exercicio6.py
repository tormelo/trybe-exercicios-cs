def find_first_fail_index(bool_list):
    start_index = 0
    end_index = len(bool_list) - 1

    while end_index >= start_index:
        mid_index = (end_index + start_index) // 2

        if bool_list[mid_index] is False:
            end_index = mid_index - 1
        else:
            start_index = mid_index + 1

    return start_index


list1 = [True, True, True, True, False, False, False]
list2 = [True, True, False, False, False, False, False]

print("Saída list1:", find_first_fail_index(list1))
print("Saída list2:", find_first_fail_index(list2))
