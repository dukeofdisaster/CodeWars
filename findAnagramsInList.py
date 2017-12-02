# This problem is similar to a previous one, finding anagrams
# but we have to treturn a list of anagrams, if they exist in a
# given list of words.
def anagrams(word, words):
    return [i for i in words if sorted(i) == sorted(word)]
