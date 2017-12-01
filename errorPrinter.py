# For this challenge we had to define
# a function that takes in strings which represent printer
# error codes. If there are errors, the string will contain
# letters m-z any number of times.
#
# We're basically comparing idnividual characters of strings
# a novice solution is below.

def printerErrors(s):
    length = str(len(s))
    badCount = 0
    badChars = "nopqrstuvwxyz"
    for _ in s:
        if _ in badChars:
            badCount += 1
    return str(badCount)+"/"+length

print(printerErrors("helloz"))

# The expert solution makes use of:
# format()
# len()
# sub()
# to construct a one liner solution
#
# re.sub(pattern, repl, string, count=0, flags=0)
# Return the string obtained by replacing the leftmost non-overlapping
# occurrences of pattern in string by the replacement repl.
# If the pattern isn’t found, string is returned unchanged. repl can be
#  a string or a function; if it is a string, any backslash escapes in
# it are processed. That is, \n is converted to a single newline
# character, \r is converted to a carriage return, and so forth.
# Unknown escapes such as \j are left alone. Backreferences, such as \6
# are replaced with the substring matched by group 6 in the pattern.
from re import sub
def printer_error(s):
    # So here we have a string with two format brackets {} {}
    # format() replaces the {} with the two values supplied
    # the first being the length of the string returned by sub()
    # which, replaces any occurences of substrings of the range
    # a-m, in s with '', essentially stripping it to contian only
    # bad characters. Uncomment to test the functionality of sub()

    #return sub("[a-m]", '', s)
    return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))

print(printer_error("aaaxyz"))
