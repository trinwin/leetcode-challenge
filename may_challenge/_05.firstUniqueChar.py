# ----------------------------------------------------------------------
# Name:        First Unique Character in a String
# Author(s):   Trinity Nguyen
# ----------------------------------------------------------------------

"""
    Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

    Examples:
    s = "leetcode"
    return 0.

    s = "loveleetcode",
    return 2.
    
    Note: You may assume the string contain only lowercase letters.
"""
import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_counter = collections.Counter(s)
        for k, v in char_counter.items():
            if (v == 1):
                return s.index(k)
        return -1
