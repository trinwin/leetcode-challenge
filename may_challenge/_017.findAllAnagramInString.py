# ----------------------------------------------------------------------
# Name:         Find All Anagrams in a String
# Author(s):    Trinity Nguyen
# ----------------------------------------------------------------------

"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.

Example 1:
Input:
s: "cbaebabacd" p: "abc"
Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input:
s: "abab" p: "ab"
Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_counter = Counter(p)
        res = []

        for i in range(len(s)-len(p)+1):
            if i == 0:
                s_counter = Counter(s[:len(p)])
            else:
                s_counter[s[i-1]] -= 1
                if not s_counter[s[i-1]]:
                    del s_counter[s[i-1]]
                s_counter[s[i+len(p)-1]] += 1

            if len(p_counter - s_counter) == 0:
                res.append(i)

        return res

    def findAnagrams2(self, s: str, p: str) -> List[int]:
        hashp = sum(hash(ch) for ch in p)
        hashi = sum(hash(ch) for ch in s[:len(p)])

        ret = []
        if hashi == hashp:
            ret.append(0)

        for idx, (ch_out, ch_in) in enumerate(zip(s, s[len(p):]), 1):
            hashi += hash(ch_in) - hash(ch_out)
            if hashi == hashp:
                ret.append(idx)

        return ret

    def findAnagrams3(self, s: str, p: str) -> List[int]:
        res = []
        n, m = len(s), len(p)
        if n < m:
            return res
        p_hash, s_hash = [0]*123, [0]*123
        for x in p:
            p_hash[ord(x)] += 1
        for x in s[:m-1]:
            s_hash[ord(x)] += 1
        for i in range(m-1, n):
            s_hash[ord(s[i])] += 1
            if i-m >= 0:
                s_hash[ord(s[i-m])] -= 1
            if shash == p_hash:
                res.append(i - m + 1)
        return res

    def findAnagrams4(self, s: str, p: str) -> List[int]:
        sol = []

        s_size = len(s)
        p_size = len(p)

        if p_size > s_size:
            return sol

        p_count = [0 for x in range(26)]
        s_count = p_count[:]

        for char in p:
            p_count[ord(char) - ord('a')] += 1

        # print(p_count)
        # print(s_count)

        for i in range(0, p_size):
            char = s[i]
            s_count[ord(char) - ord('a')] += 1

        # print(s_count)

        if p_count == s_count:
            sol.append(0)

        for i in range(1, s_size-p_size+1):
            old_char = s[i-1]
            s_count[ord(old_char) - ord('a')] -= 1

            char = s[i+p_size-1]
            s_count[ord(char) - ord('a')] += 1

            # print("{}: {}".format(i, s_count))
            if p_count == s_count:
                sol.append(i)

        return sol
