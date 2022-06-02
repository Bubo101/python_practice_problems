# Write a function that meets these requirements.
#
# Name:       sum_fraction_sequence
# Parameters: a number
# Returns:    the sum of the fractions of the
#             form 1/2+2/3+3/4+...+number/number+1
#
# Examples:
#     * input:   1
#       returns: 1/2
#     * input:   2
#       returns: 1/2 + 2/3
#     * input:   3
#       returns: 1/2 + 2/3 + 3/4 in decimal answer
#return sum of fractions

def sum_fraction_sequence(n):
    sum = 0
    for i in range (1, n + 1):
        # plus = adds to the sum rather than using = only, sum = sum + (1/(i +1 )) is what it equates too
        sum += i / (i + 1)
    return sum

print(sum_fraction_sequence(5))

