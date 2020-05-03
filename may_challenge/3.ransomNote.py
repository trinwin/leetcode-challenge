
# ----------------------------------------------------------------------
# Name:        Ransom Note
# Author(s):   Trinh Nguyen
# ----------------------------------------------------------------------

"""
    Given an arbitrary ransom note string and another string containing letters from all the magazines, 
    write a function that will return true if the ransom note can be constructed from the magazines ; 
    otherwise, it will return false.

    Each letter in the magazine string can only be used once in your ransom note.

    Note:
    You may assume that both strings contain only lowercase letters.

    Example:
    canConstruct("a", "b") -> false
    canConstruct("aa", "ab") -> false
    canConstruct("aa", "aab") -> true
"""

import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        :param ransomNote (string):
        :param magazine (string): string containing letters from all the magazine
        :return (boolean): True if the ransom note can be constructed from the magazines 
            otherwise, it will return False
        """
        for letter in ransomNote:
            if not letter in magazine:
                return False
            magazine = magazine.replace(letter, "", 1)
        return True

    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        """
        Another solution using set
        """
        ransom_set = set(ransomNote)
        for letter in ransom_set:
            if ransomNote.count(letter) > magazine.count(letter):
                return False
        return True

    def canConstruct3(self, ransomNote: str, magazine: str) -> bool:
        """
        Another solution using Counter collection
        """
        count_r = collections.Counter(ransomNote)
        count_m = collections.Counter(magazine)
        for char in count_r:
            if count_r[char] > count_m[char]:
                return False
        return True
