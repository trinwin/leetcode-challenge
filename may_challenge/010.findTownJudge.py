# ----------------------------------------------------------------------
# Name:        Find the Town Judge
# Author(s):   Trinity Nguyen
# ----------------------------------------------------------------------

"""
   In a town, there are N people labelled from 1 to N.  
   There is a rumor that one of these people is secretly the town judge.

    If the town judge exists, then:

    The town judge trusts nobody.
        1. Everybody (except for the town judge) trusts the town judge.
        2. There is exactly one person that satisfies properties 1 and 2.
        3. You are given trust, an array of pairs trust[i] = [a, b] 
        representing that the person labelled a trusts the person labelled b.

    If the town judge exists and can be identified, return the label of the town judge.  
    Otherwise, return -1.

    Example 1:
    Input: N = 2, trust = [[1,2]]
    Output: 2

    Example 2:
    Input: N = 3, trust = [[1,3],[2,3]]
    Output: 3

    Example 3:
    Input: N = 3, trust = [[1,3],[2,3],[3,1]]
    Output: -1

    Example 4:
    Input: N = 3, trust = [[1,2],[2,3]]
    Output: -1

    Example 5:
    Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
    Output: 3
    

    Note:
    1 <= N <= 1000
    trust.length <= 10000
    trust[i] are all different
    trust[i][0] != trust[i][1]
    1 <= trust[i][0], trust[i][1] <= N

"""


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust) < N - 1:
            return -1

        trusted_by = [0] * (N + 1)  # trusted by others
        trusters = [0] * (N + 1)   # trust others

        for a, b in trust:
            trusters[a] += 1
            trusted_by[b] += 1

        for i in range(1, N+1):
            if(trusted_by[i] == N-1 and trusters[i] == 0):
                return i

        return -1

    def findJudge2(self, N: int, trust: List[List[int]]) -> int:
        trusters = {x[0] for x in trust}
        trusted_by = 0
        candidate = -1
        for i in range(1, N+1):
            if i not in trusters:
                candidate = i

        for a, b in trust:
            if b == candidate:
                trusted_by += 1

        if trusted_by != N - 1:
            candidate = -1

        return candidate
