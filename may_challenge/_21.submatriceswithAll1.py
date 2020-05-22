# ----------------------------------------------------------------------
# Name:        Count Square Submatrices with All Ones
# Author(s):   Trinity Nguyen
# ----------------------------------------------------------------------

"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example 1:
Input: matrix =
    [
    [0,1,1,1],
    [1,1,1,1],
    [0,1,1,1]
    ]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.

Example 2:
Input: matrix = 
    [
    [1,0,1],
    [1,1,0],
    [1,1,0]
    ]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
 

Constraints:
    1. 1 <= arr.length <= 300
    2. 1 <= arr[0].length <= 300
    3. 0 <= arr[i][j] <= 1

Hint:
    1. Create an additive table that counts the sum of elements of submatrix with the superior corner at (0,0).
    2. Loop over all subsquares in O(n^3) and check if the sum make the whole array to be ones, if it checks then add 1 to the answer.
"""


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        count = 0
        r = len(matrix)
        c = len(matrix[0])
        for i in range(r):
            count += matrix[i][0]

        for j in range(1, c):
            count += matrix[0][j]

        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][j] == 1:
                    matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])+1
                    count += matrix[i][j]
        return count

    def countSquares2(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] and matrix[i][j-1] and matrix[i-1][j-1]:
                    k = min(matrix[i-1][j], matrix[i][j-1])
                    matrix[i][j] = k+1 if matrix[i-k][j-k] else k

        return sum(sum(row) for row in matrix)
