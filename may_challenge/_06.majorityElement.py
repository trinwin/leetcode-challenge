# ----------------------------------------------------------------------
# Name:        Majority Element
# Author(s):   Trinity Nguyen
# ----------------------------------------------------------------------

"""
    Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

    You may assume that the array is non-empty and the majority element always exist in the array.

    Example 1:
    Input: [3,2,3]
    Output: 3

    Example 2:
    Input: [2,2,1,1,1,2,2]
    Output: 2
"""
import collections


class Solution:
    def majorityElement(self, nums: collections.List[int]) -> int:
        counter = collections.Counter(nums)
        return max(counter, key=lambda c: counter[c] > (len(nums)/2))

    def majorityElement2(self, nums: collections.List[int]) -> int:
        for i in set(nums):
            if nums.count(i) > len(nums)/2:
                ans = i
                break
        return ans

    def majorityElement3(self, nums: collections.List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]  # Median of the array
