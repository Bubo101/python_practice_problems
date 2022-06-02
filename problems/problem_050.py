# Write a function that meets these requirements.
#
# Name:       halve_the_list
# Parameters: a single list
# Returns:    two lists, each containing half of the original list
#             if the original list has an odd number of items, then
#             the extra item is in the first list
#
# Examples:
#    * input: [1, 2, 3, 4]
#      result: [1, 2], [3, 4]
#    * input: [1, 2, 3]
#      result: [1, 2], [3]

import math

def halve_the_list(list1):
    half_list_length = math.ceil(len(list1)/2)
    print(int(half_list_length))
    first_list = list1[:int(half_list_length)]
    second_list = list1[int(half_list_length):]
    return first_list, second_list

print(halve_the_list([1,2,3,4,5]))