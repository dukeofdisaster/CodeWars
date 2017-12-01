# regex validate pin code challenge
#
# For this challenge we had to take in a pin
# then verify that it was of length 4 or 6 and that it was
# all digits. For this one we made use of the sub function again
# thinking we were clever but there was an even simpler solution

from re import sub
def validate_pin(pin):
    if not (len(pin) == 4 or len(pin) == 6):
        return False
    return (''== sub("[0-9]", '', pin))

# The expert example didn't require any imports
# and outsmarted the creator as no regex was necessary.
# it only used built-in functions and Python features

def validate(pin):
    # this is slightly deceiving and easy to forget
    # we are used to seeing in range() which gives us range of
    # numbers, but supplied a parenthetical statement, the logic
    # treats (4, 6) as an array
    return len(pin) in (4, 6) and pin.isdigit()

print(validate("12345"))
