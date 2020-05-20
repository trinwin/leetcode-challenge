# ----------------------------------------------------------------------
# Name:         Single Element in a Sorted Array
# Author(s):   Trinity Nguyen
# ----------------------------------------------------------------------

"""
   You are given a sorted array consisting of only integers where every element appears exactly twice, 
   except for one element which appears exactly once. Find this single element that appears only once.  
    
    Example 1:

    Input: [1,1,2,3,3,4,4,8,8]
    Output: 2
    Example 2:

    Input: [3,3,7,7,10,11,11]
    Output: 10
    

    Note: Your solution should run in O(log n) time and O(1) space.

"""


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for i in range(0, len(nums), 2):
            if i+1 < len(nums) and nums[i] != nums[i+1]:
                return nums[i]
            elif i + 1 == len(nums):
                return nums[i]

    def singleNonDuplicate2(self, nums: List[int]) -> int:
        return sum(set(nums))*2-sum(nums)

    def singleNonDuplicate3(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        while True:
            mid = (low + high) // 2
            if mid % 2 == 1:
                mid -= 1
            if mid < high and nums[mid] == nums[mid+1]:
                low = mid + 2
            elif mid > low and nums[mid] == nums[mid-1]:
                high = mid - 2
            else:
                return nums[mid]
