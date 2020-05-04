# ----------------------------------------------------------------------
# Name:        Number Complement
# Author(s):   Trinh Nguyen
# ----------------------------------------------------------------------

"""
    Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

    Example 1:
    Input: 5
    Output: 2
    Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

    Example 2:
    Input: 1
    Output: 0
    Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.


    Note:

    1. The given integer is guaranteed to fit within the range of a 32-bit signed integer.
    2. You could assume no leading zero bit in the integer’s binary representation.
    3. This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/
"""


class Solution:
    def findComplement(self, num: int) -> int:
        """
        :param num (int): a number
        :return (int): complement of num
        """
        binary = bin(num)
        comp = ''.join(['0' if c == '1' else '1' for c in binary[2:]])
        return (int(comp, 2))

    def findComplement2(self, num: int) -> int:
        """
        Another solution using list comprehension
        """
        binary = bin(num)
        comp = ""
        for digit in binary[2::]:
            if (digit == '0'):
                comp += '1'
            elif (digit == '1'):
                comp += '0'
        return int(comp, 2)
