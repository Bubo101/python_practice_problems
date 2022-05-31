# Complete the calculate_sum function which accepts
# a list of numerical values and returns the sum of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#

def calculate_sum(values):
    if len(values) == 0:
        return None
    sum = 0
    for item in values:
        sum = sum + item 
    return sum
    
print(calculate_sum([2,3,4]))
