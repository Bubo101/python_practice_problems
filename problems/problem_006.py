# Complete the can_skydive function so that determines if
# someone can go skydiving based on these criteria
#
# * The person must be greater than or equal to 18 years old, or
# * The person must have a signed consent form

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

from operator import truediv


def can_skydive(age, has_consent_form):
    if age >= 18 or has_consent_form == True:
        return True
    else:
        return False 

age1 = 5
consent_form = True

firstresult = can_skydive(age1,consent_form)
print(firstresult)

#conditions:  age greater or equal to 18 or signed consent form
#pseudo code:  we have ages and consent form, if person is over 18 
#has a signed form we they can go /it shoudl return true
# age_one = 25, has_consent_form = True