# Complete the has_quorum function to test to see if the number
# of the people in the attendees list is greater than or equal
# to 50% of the number of people in the members list.
# has quorum functionw ith two variables attendees and members:
    #if attendees is greater than or equal to 50% of members
        #return true 

def has_quorum(attendees_list, members_list):
    num_attend = len(attendees_list)
    num_members = len(members_list)
    if num_attend / num_members >= 0.5:
        return True
    else:
        return False 
    

print(has_quorum(["george", "orion", "brock"], ["george", "orion", "brock", "linda", "josiah", "arnold"]))
