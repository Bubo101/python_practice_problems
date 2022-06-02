# Complete the check_password function that accepts a
# single parameter, the password to check.
#
# A password is valid if it meets all of these criteria
#   * It must have at least one lowercase letter (a-z)
#   * It must have at least one uppercase letter (A-Z)
#   * It must have at least one digit (0-9)
#   * It must have at least one special character $, !, or @
#   * It must have six or more characters in it
#   * It must have twelve or fewer characters in it
#
# The string object has some methods that you may want to use,
# like ".isalpha", ".isdigit", ".isupper", and ".islower"


def check_password(password):
    special = ["$","!","@"]
    l = 0
    u = 0
    a = 0
    d = 0
    s = 0
    if len(password) >= 6 and len(password) <= 12:
        for c in password:
            if c.isalpha():
                a += 1
            if c.isdigit():
                d += 1
            if c.isupper():
                u += 1
            if c.islower():
                l += 1
            if c in special:
                s += 1
    if l >= 1 and u >= 1 and a >= 1 and d >= 1 and s >= 1:
        print("Valid Password")
    else:
        print("Invalid Password")

check_password("Boden198$")
        
            
