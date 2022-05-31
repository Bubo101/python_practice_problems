# Complete the calculate_average function which accepts
# a list of numerical values and returns the average of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#
# Pseudocode is available for you

#Function accepts a list "values" and returns average of the numbers 
    #if numbers in values > 0:
    # return sum of numbers

def calculate_average(values):
    if len(values) ==0:
        return None
    sum = 0
    for item in values:
        sum = sum + item
    return sum / len(values) 

print("average", calculate_average([2,3,4,5,12]))