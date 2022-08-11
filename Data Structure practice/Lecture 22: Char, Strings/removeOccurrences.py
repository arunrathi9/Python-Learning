# Leetcode problem - Remove all occurrences of a substring

import re

def removeOccurrences(s, part):

    #while(re.search(part, s)):
    while part in s:
        s = re.sub(part, "", s, count=1)

    return s

print(removeOccurrences('daabcbaabcbc', 'abc'))
print(removeOccurrences('aabababa', 'aba'))
print(removeOccurrences('axxxxyyyyb', 'xy'))
