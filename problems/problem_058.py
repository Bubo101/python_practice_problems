# Write a function that meets these requirements.
#
# Name:       group_cities_by_state
# Parameters: a list of cities in the format "«name», «st»"
#             where «name» is the name of the city, followed
#             by a comma and a space, then the two-letter
#             abbreviation of the state
# Returns:    a dictionary whose keys are the two letter
#             abbreviations of the states in the list and
#             whose values are a list of the cities appearing
#             in that list for that state
#
# In the items in the input, there will only be one comma.
#
# Examples:
#     * input:   ["San Antonio, TX"]
#       returns: {"TX": ["San Antonio"]}
#     * input:   ["Springfield, MA", "Boston, MA"]
#       returns: {"MA": ["Springfield", "Boston"]}
#     * input:   ["Cleveland, OH", "Columbus, OH", "Chicago, IL"]
#       returns: {"OH": ["Cleveland", "Columbus"], "IL": ["Chicago"]}
#
# You may want to look up the ".strip()" method for the string. This has an optional paramater that will pass strip and contain characters you want to strip to

#other sln
# def group_cities_by_state(cities):
#     cities_and_states = {}

#     for each in cities:
#         key = each.split(", ")[1]
#         value = each.split (", ")[0]
#         if key not in cities_and_states:
#             cities_and_states[key]=[value]
#         else:
#             cities_and_states[key].append(value)
#     return cities_and_states
# print(group_cities_by_state(["Cleveland, OH", "Columbus, OH", "Chicago, IL"]))


def group_cities_by_state(cities):          # solution
    output = {}                             # solution
    for city in cities:                     # solution
        name, state = city.split(",")       # solution
        state = state.strip()               # solution
        if state not in output:             # solution
            output[state] = []              # solution
        output[state].append(name)          # solution
    return output                           # solution
print(group_cities_by_state(["Cleveland, OH", "Columbus, OH", "Chicago, IL"]))