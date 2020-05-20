# ----------------------------------------------------------------------
# Name:         Permutation in String
# Author(s):    Trinity Nguyen
# ----------------------------------------------------------------------

"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
In other words, one of the first string's permutations is the substring of the second string.

Example 1:
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""
import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = collections.Counter(s1)

        for i in range(len(s2)-len(s1)+1):
            if i == 0:
                s2_counter = Counter(s2[:len(s1)])
            else:
                s2_counter[s2[i-1]] -= 1
                if not s_counter[s[i-1]]:
                    del s_counter[s[i-1]]
                s2_counter[s2[i+len(s1)-1]] += 1

            if len(s1_counter - s2_counter) == 0:
                return True

        return False

    def checkInclusion2(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        if l1 == 0 and l2 == 0:
            return False
        if l2 < l1:
            return False

        a1 = [0 for i in range(26)]
        a2 = [0 for i in range(26)]
        a = ord('a')
        for c in s1:
            a1[ord(c) - a] += 1
        for c in s2[:len(s1)]:
            a2[ord(c) - a] += 1
        if a1 == a2:
            return True

        for i in range(l2 - l1):
            a2[ord(s2[i]) - a] -= 1
            a2[ord(s2[i + l1]) - a] += 1
            if a1 == a2:
                return True
