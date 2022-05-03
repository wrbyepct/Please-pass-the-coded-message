
# mock_list = [0]
# mock_list_2 = [3, 3, 3, 3]
# mock_list_3 = [2, 9, 9, 9, 9, 9, 1, 1]
# mock_list_4 = [1, 1, 2, 8, 3, 4, 7]
# mock_list_5 = [1, 1, 1, 2, 0, 0, 0, 8]
# mock_list_6 = [7, 1, 1, 1]
# mock_list_7 = [1, 7, 3]
# mock_list_8 = [1, 4, 0, 3]
# mock_list_9 = [5, 2, 1]
# mock_list_10 = [5, 2, 3]
# mock_list_11 = [2, 2, 8, 8]
# mock_list_12 = [1, 1, 1, 1, 4]
# mock_list_13 = [2, 2, 2, 2, 8, 1, 1, 1, 4]
# mock_list_14 = [1, 1, 1, 1, 1, 1, 1, 4]
# mock_list_15 = [4, 4, 4, 4, 4]
# mock_list_16 = [4, 4, 2, 2, 3]

# extra = 2
mock_list_1 = [1, 1, 1, 1, 4, 0, 3, 0, 0]
mock_list_2 = [2, 2, 8, 8]
mock_list_3 = [4, 4, 4, 5]
mock_list_4 = [4, 4, 4, 8]
mock_list_5 = [7, 7, 7, 7, 7]
mock_list_6 = [4, 4, 4, 4, 4]
mock_list_7 = [4, 7, 7, 7, 7]
mock_list_8 = [1, 4, 4, 4, 4]
mock_list_9 = [1, 7, 7, 7, 7]
mock_list_16 = [4, 7, 4, 7, 4, 7, 4, 7]

# Extra value = 1
# 2 extra 2 number causes extra 1
mock_list_10 = [2, 8]
mock_list_14 = [2, 5]
# 4 causes extra 1
mock_list_11 = [4, 4, 5]
# 7 causes extra 1
mock_list_12 = [2, 5, 8, 7]
# 1 causes extra 1
mock_list_13 = [1, 7, 7, 4]

mock_list_15 = [2, 5, 2, 5, 2, 5, 2, 5]

"""
Important question!  
What if the extra value is 1, but 1, 4, 7 are no where to be found!
"""


# Patterns:
#    1. There could be 1 number that makes remainder either 1 or 2 (4 -> 1 or 8 -> 2 etc)
#    2. If not there could be 2 numbers that make remainder either 1 or 2 (1, 4 -> 2 or 5, 8, -> 1 etc)
def solution(the_list):
    # Split the list into two groups:
    #     One is divisible by 3
    #     The other is not
    new_number_list = []   # Divisible by 3
    examine_list = []      # Not divisible by 3
    for n in the_list:
        if n % 3 != 0:
            examine_list.append(n)
        else:
            new_number_list.append(n)

    # If the examined list is not empty
    if examine_list:
        # Get the correct pruned list of examined list
        examine_list = get_pruned_examine_list(sorted(examine_list))
        return get_final_number(new_number_list + examine_list)

    return get_final_number(new_number_list)


def get_pruned_examine_list(examine_list):
    # Get the sum of the new list
    list_sum = sum(examine_list)
    # The extra value that causes the number is not 3 divisible
    extra_value = list_sum % 3

    # Get rid of list that is too small to arrange a 3 divisible number
    if len(examine_list) < 3 and extra_value != 0:
        return []
    # If the sum cannot be divided by 3, there must be numbers need to be removed
    if extra_value != 0:
        return prune_list(examine_list, extra_value)

    return examine_list


def get_final_number(new_number_list):
    # If there is no number return 0
    if not new_number_list:
        return 0
    # Put bigger numbers to the front
    new_number_list.sort(reverse=True)

    final_number = 0
    for n in new_number_list:
        final_number = final_number * 10 + n

    return final_number


def prune_list(examine_list, extra_value):
    if extra_value == 2:
        examine_list = prune_extra_two(examine_list)

    if extra_value == 1:
        examine_list = prune_extra_one(examine_list)

    return examine_list


def prune_extra_two(examine_list):
    for n in examine_list:
        if n == 2 or n == 5 or n == 8:
            examine_list.remove(n)
            return examine_list

    # If it reaches this point, it means there are two numbers like 1, 4, 7 that causes extra value equals 2
    return prune_extra_one(examine_list)


def prune_extra_one(examine_list):
    # Deal with normal case
    for n in examine_list:
        if n == 1 or n == 4 or n == 7:
            examine_list.remove(n)
            return get_pruned_examine_list(examine_list)

    # If it reaches this point, it's a special case:
    #    that is, for example, the extra value is 2, but 1, 4, 7 are nowhere to be found!
    return remove_first_element(examine_list)


def remove_first_element(examine_list):
    examine_list.remove(examine_list[0])
    return get_pruned_examine_list(examine_list)


def print_result(final_number):
    print(f"This is the final number: {final_number}")


print_result(solution(mock_list_1))
print_result(solution(mock_list_2))
print_result(solution(mock_list_3))
print_result(solution(mock_list_4))
print_result(solution(mock_list_5))
print_result(solution(mock_list_6))
print_result(solution(mock_list_7))
print_result(solution(mock_list_8))
print_result(solution(mock_list_9))
print_result(solution(mock_list_10))
print_result(solution(mock_list_11))
print_result(solution(mock_list_12))
print_result(solution(mock_list_13))
print_result(solution(mock_list_14))
print_result(solution(mock_list_15))
print_result(solution(mock_list_16))






















