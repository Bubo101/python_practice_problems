# Write a function that meets these requirements.
#
# Name:       simple_roman
# Parameters: one parameter that has a value from 1
#             to 10, inclusive
# Returns:    the Roman numeral equivalent of the
#             parameter value
#
# All examples
#     * input: 1
#       returns: "I"
#     * input: 2
#       returns: "II"
#     * input: 3
#       returns: "III"
#     * input: 4
#       returns: "IV"
#     * input: 5
#       returns: "V"
#     * input: 6
#       returns: "VI"
#     * input: 7
#       returns: "VII"
#     * input: 8
#       returns: "VIII"
#     * input: 9
#       returns: "IX"
#     * input: 10
#       returns:  "X"

def simple_roman(value1):
    if value1 == 1:
        return "I"
    elif value1 == 2:
        return "II"
    elif value1 == 3:
        return "III"
    elif value1 == 4:
        return "IV"
    elif value1 == 5:
        return "V"
    elif value1 == 6:
        return "VI"
    elif value1 == 7:
        return "VII"
    elif value1 == 8:
        return "VIII"
    elif value1 == 9:
        return "IX"
    elif value1 == 10:
        return "X"
    else:
        return ValueError
print(simple_roman(5))