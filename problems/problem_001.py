# Complete the minimum_value function so that returns the
# minimum of two values.
#
# If the values are the same, return either.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def minimum_value(value1, value2):
    if value1 < value2:
        return value1
    return value2
    
    pass
#what is the input:  2 values
#what is the output?  minimum of the two values
#conditions? if a < b (implied condition, 
    #  what needs to be done depending on information)
    # it will either be one input or the other, no other options
#pseudocode: try to find minimum value of 2 inputs
    #if a is less than be, return that value
    #if it isn't, return the other value