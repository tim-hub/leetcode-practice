#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (53.64%)
# Likes:    3249
# Dislikes: 108
# Total Accepted:    689.4K
# Total Submissions: 1.2M
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
#
# Example:
#
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
# Note:
#
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
#
#

# @lc code=start
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         for ii in range(i+1, len(nums)):
        #             if (nums[ii] != 0):
        #                 tmp = nums[ii]
        #                 nums[ii] = nums[i]
        #                 nums[i] = tmp
        #                 break
        #             # out of the loop

        # https://leetcode.com/problems/move-zeroes/discuss/563755/Easy-Python-O(N)-Beats-97-Of-Solutions-in-Runtime
        count = 0
        i = 0
        length = len(nums)
        while i < length:
            if nums[i] == 0:
                count += 1
                nums.pop(i)
                length -= 1
                i -= 1
            i += 1
        nums += [0]*count

        return None

# @lc code=end


nums = [0, 1, 0, 3, 12]
print(nums)
Solution.moveZeroes(nums=nums)
print(nums)
