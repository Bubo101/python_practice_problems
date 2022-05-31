# Complete the max_in_list function to find the
# maximum value in a list
#
# If the list is empty, then return None.
#

def max_in_list(values):
    maxnum = 0
    if len(values) == 0:
        return None 
    for num in values:
        if num > maxnum:
            maxnum = num
    return maxnum

print(max_in_list([1,2,3,4,5,6,12]))
