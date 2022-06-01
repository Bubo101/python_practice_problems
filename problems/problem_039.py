# Complete the reverse_dictionary function which has a
# single parameter that is a dictionary. Return a new
# dictionary that has the original dictionary's values
# for its keys, and the original dictionary's keys for
# its values.
#
# Examples:
#   * input:  {}
#     output: {}
#   * input:  {"key": "value"}
#     output: {"value", "key"}
#   * input:  {"one": 1, "two": 2, "three": 3}
#     output: {1: "one", 2: "two", 3: "three"}

def reverse_dictionary(dictionary):
    new_dictionary = {}
    for key, value in dictionary.items():
        #grabbing the key and the value
        new_dictionary[value] = key
        #set the value to the key
    return new_dictionary




print(reverse_dictionary({"booty":"1","shark":"2","plantain":"3"}))
