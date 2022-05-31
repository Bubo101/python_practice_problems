# Complete the calculate_grade function which accepts
# a list of numerical scores each between 0 and 100.
#
# Based on the average of the scores, the function
# returns
#   * An "A" for an average greater than or equal to 90
#   * A "B" for an average greater than or equal to 80
#     and less than 90
#   * A "C" for an average greater than or equal to 70
#     and less than 80
#   * A "D" for an average greater than or equal to 60
#     and less than 70
#   * An "F" for any other average

#There is a list of scores between 0 and 100
#take an average of the list

def calculate_grade(values):
    average_list = sum(values)/len(values)
    if average_list >= 90:
        return "A"
    elif average_list >= 80:
        return "B"
    elif average_list >= 70:
        return "C"
    elif average_list >= 60:
        return "D"
    else:
        return "F"

print(calculate_grade([80,90,95,97,54,64,51]))