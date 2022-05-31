# Complete the count_letters_and_digits function which
# accepts a parameter s that contains a string and returns
# two values, the number of letters in the string and the
# number of digits in the string
#
# Examples:
#   * "" returns 0, 0
#   * "a" returns 1, 0
#   * "1" returns 0, 1
#   * "1a" returns 1, 1
#
# To test if a character c is a digit, you can use the
# c.isdigit() method to return True of False
#
# To test if a character c is a letter, you can use the
# c.isalpha() method to return True of False
#
# Remember that functions can return more than one value
# in Python. You just use a comma with the return, like
# this:
#      return value1, value2
# Function accepts a string "s" and determines how many letters or numbers are there


def count_letters_and_digits(s):
    value1 = 0
    value2 = 0
    for character in s:
        if character.isdigit():
            value1 = value1 + 1
        if character.isalpha():
            value2 = value2 + 1
    return value2, value1 

print(count_letters_and_digits("Julie101"))
