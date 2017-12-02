# In this challenge we have to define a function that checks
# if two strings are anagrams, that is, if they both contain the same
# letters (non case-sensitive).
#
# The novice solution uses a loop structure
def is_anagram(test, original):
    good = True
    for x in test.lower():
        if test.lower().count(x) > original.lower().count(x) or len(test) != len(original):
            good = False
    return good

# Expert solution makes use of the built-in funciton sorted()
# Since anagrams should have the exact same length, they should be
# equal to each other when sorted
def is_anagram(test, original):
    return sorted(original.lower()) == sorted(test.lower())
