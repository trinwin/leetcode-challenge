# ----------------------------------------------------------------------
# Name:        Valid Perfect Square
# Author(s):   Trinity Nguyen
# ----------------------------------------------------------------------

"""
    Given a positive integer num, write a function which returns True if num is a perfect square else False.

    Note: Do not use any built-in library function such as sqrt.

    Example 1:
    Input: 16
    Output: true

    Example 2:
    Input: 14
    Output: false

"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while (i * i < num):
            i += 1

        return i * i == num

    def isPerfectSquare2(self, num: int) -> bool:
        a = num**0.5
        if a == int(a):
            return True
        else:
            return False
