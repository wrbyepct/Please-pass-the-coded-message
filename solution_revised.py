"""
Informal Structured Outline

Problem type:
   Matching the restrictions


The gist of the problem:
    Give a list of 1 - digit numbers,
    return the largest number that is form by digits in the list,
    and it is also divisible by 3


Input range:
    List of integer
    0 ≤ element range ≤ 9
    1 ≤ list size ≤ 9


Mainly concerned target:
   Non-divisible-by-3-digits list like [1, 4, 7, 2, 5, 8]


Goal:
   From those non-divisible-by-3-digits,
   find the largest number combination that is divisible by 3 if possible
   E.g.
        Given [1, 4, 7, 2, 8]
        then we should find 8742

What we have known:
    1. First we examine if the raw is already divisible by 3, if yes just sort the list and return the number
    2. Then if not there are only 2 cases:
            remainder = 1
            remainder = 2
    3. The raw list can contain numbers like 3, 6, 9, 0 which are already divisible by 3 in any combinations,
        so we can move them to another list.

    4. Now we only have to deal with numbers like 1, 4, 7, 2, 5, 8

    5. If the remainder is 1 ->
            a. meaning there are at least 1 digit of(1 or 4 or 7), which I will later call it one
            b. There are no ones, meaning there are 2 digits of (2, 5, 8) of any possible combination
    6. If the remainder is 2 ->
            a. meaning there are at least 1 digit of(2 or 5 or 8), which I will later call it two
            b. There are no twos, meaning there are 2 ones of any possible combination


Conclusion:
   1. We just need to separate the lists and deal with list of [8, 7, 5, 4, 2, 1](sorted from biggest to smallest)
   2. If the remainder is 1 ->
            a. Find a one and remove it
            b. If they don't exist then simply remove the last two digits(the smallest 2)
   3. If the remainder is 2 ->
            a. Find a two and remove it
            b. If they don't exist then simply remove the last two digits(the smallest 2)

   4. Combine the 3_list and none_3_list and sort it and calculate the result


Must do in order to achieve the goal:
    There are 2 mian possible cases need to be addressed when the remainder is not 0:
     Type     3_list     non_3_list
     -------------------------------
      1.        Ø         size ≤ 2
      2.      Ø ∨ ¬Ø      size > 2
                        (remainder 1: a. extra 1 one ∨ b. extra 2 twos
                         remainder 2: a. extra 1 two ∨ b. extra 2 ones)


===============================================================


Formal Description

**The specs only describe the logic to make the list divisible by 3, and match the requirement**

-------------Definitions--------------
given_list: Int
L: List:Int
3_list: List:Int
non_3_lst: List
final_number: Int
remainder: Int

---------------Steps-------------------
L := given_list
remainder := getRemainder(L)
{ L ≠ Ø ∧ 0 ≤ remainder ≤ 2 }

IF
     remainder = 0 -> skip;
     remainder ≠ 0 ->
        non_3_list := getNon3List(L);
            3_list := get3List(L);

        IF
            length(non_3_list) ≤ 2 -> L := 3_list.reverseSorted  # this case is impossible to form 3 divisible
            length(non_3_list) > 2 ->
                non_3_list := non_3_list.reverseSorted;
                remainder = 1 ->
                    IF
                        ∃(1 ∨ 4 ∨ 7) ∈ non_3_list ->
                            remove_the_smallest_(1 ∨ 4 ∨ 7)(non_3_list)
                       ¬∃(1 ∨ 4 ∨ 7) ∈ non_3_list ->
                            remove_the_last_two(non_3_list)
                    FI
                remainder = 2 ->
                    IF
                        ∃(2 ∨ 5 ∨ 8 ) ∈ non_3_list ->
                            remove_the_smallest_(2 ∨ 5 ∨ 8)(non_3_list)
                       ¬∃(2 ∨ 5 ∨ 8) ∈ non_3_list ->
                            remove_the_last_two(non_3_list)
                    FI
                L := (non_3_list + 3_list).reverseSorted
        FI;
FI

{ (L = Ø ∧ divisible_by_3(L)) ∨ L = Ø }

========================================
Time complexity: Θ(n) (the calculation of the final sum)


"""



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

# No none-3
mock_list_17 = [3, 0, 6]

"""
Important question!  
What if the extra value is 1, but 1, 4, 7 are no where to be found!
"""


def solution(given_list):

    remainder = sum(given_list) % 3
    # Already divisible by 3
    if remainder == 0:
        return get_final_number(given_list)

    # At this point, there must be numbers that's causing remainder 1 or 2
    three_list = []          # Divisible by 3
    non_three_list = []      # Not divisible by 3
    # Split the into 2 lists
    for n in given_list:
        if n % 3 != 0:
            non_three_list.append(n)
        else:
            three_list.append(n)
    # If the size of non_3_list > 2
    # It only makes sense if the remaining none_3_list will not be empty
    # Which means there are at least 3 elements in the list 
    if len(non_three_list) > 2:
        non_three_list.sort(reverse=True)
        if remainder == 1:
            if 1 in non_three_list:
                non_three_list.remove(1)
            elif 4 in non_three_list:
                non_three_list.remove(4)
            elif 7 in non_three_list:
                non_three_list.remove(7)
            else:
                del non_three_list[-2:]
        else:
            if 2 in non_three_list:
                non_three_list.remove(2)
            elif 5 in non_three_list:
                non_three_list.remove(5)
            elif 8 in non_three_list:
                non_three_list.remove(8)
            else:
                del non_three_list[-2:]

        return get_final_number(three_list + non_three_list)
    # If the size of non_3_list ≤ 2
    # There are 1 or 2 numbers that are causing remainder 1 or 2
    # there are only 1 number and 2 number circumstances
    # either way, we have to remove them all
    # which will inevitably become empty list
    # So there's no reason to calculate
    # So we can just return the three list
    return get_final_number(three_list)


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
print_result(solution(mock_list_17))
