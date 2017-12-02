# scramblies.py
#
# In this challenge we have to define a function that takes two strings
# and then checks them to see if the characters from string 1, can be used
# to create string 2. The number of times the character occurs will be
# important, for example if s1 = "missip" and s2 == "mississippi",
# the function should return false.
#
#
# Below is the novice solution
def scramble(s1,s2):
    good = True
    for i in s2:
        if (s2.count(i)) > (s1.count(i)):
            good = False
    return good

# There is currently not an expert solution for this challenge
