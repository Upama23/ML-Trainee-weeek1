from collections import defaultdict

#  Given an array of strings (str), group the anagrams together. You can return the
# answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different
# word or phrase, typically using all the original letters exactly once.


def anagrams(strs):
    anagrams = defaultdict(list)
    for x in strs:
        key = ''.join(sorted(x))
        anagrams[key].append(x)
    return list(anagrams.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = anagrams(strs)
print(result)