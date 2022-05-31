# Complete the gear_for_day function which returns a list of
# gear needed for the day given certain criteria.
#   * If the day is not sunny and it is a workday, the list
#     needs to contain "umbrella"
#   * If it is a workday, the list needs to contain "laptop"
#   * If it is not a workday, the list needs to contain
#     "surfboard"
#need a gear list
#if day is sunny is false and is workday
    #list.append[umbrella]
#if workday is True

def gear_for_day(is_workday, is_sunny):
    gear_needed = []
    if is_sunny == False and is_workday == True:  
        gear_needed.append("umbrella")
    if is_workday == True:
        gear_needed.append("laptop")
    else:
        gear_needed.append("surfboard")
    return gear_needed

print(gear_for_day(True, False))
