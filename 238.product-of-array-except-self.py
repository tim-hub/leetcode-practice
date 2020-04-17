#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (53.91%)
# Likes:    4217
# Dislikes: 366
# Total Accepted:    470.1K
# Total Submissions: 793.9K
# Testcase Example:  '[1,2,3,4]'
#
# Given an array nums of n integers where n > 1,  return an array output such
# that output[i] is equal to the product of all the elements of nums except
# nums[i].
#
# Example:
#
#
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
#
#
# Constraint: It's guaranteed that the product of the elements of any prefix or
# suffix of the array (including the whole array) fits in a 32 bit integer.
#
# Note: Please solve it without division and in O(n).
#
# Follow up:
# Could you solve it with constant space complexity? (The output array does not
# count as extra space for the purpose of space complexity analysis.)
#
#

# @lc code=start
from operator import mul


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if not 0 in nums:
            prod = reduce(mul, nums, 1)
            return list(map(lambda x: int(prod/x), nums))
        else:
            the_nums = list(filter(lambda x: x != 0, nums))

            if len(the_nums) == 0 or len(nums)-len(the_nums) >= 2:
                prod = 0

            else:
                prod = reduce(mul, the_nums, 1)

            return list(map(lambda x: 0 if x != 0 else prod, nums))


# @lc code=end
