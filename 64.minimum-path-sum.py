#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (45.59%)
# Likes:    2474
# Dislikes: 53
# Total Accepted:    360K
# Total Submissions: 685.7K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
# Example:
#
#
# Input:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
#
#
#

# @lc code=start


class Solution:

    def minPathSum(self, grid: List[List[int]]) -> int:

        r = len(grid)
        if r == 0:
            return 0
        c = len(grid[0])
        if c == 0:
            return 0
        cache = {(0, 0): grid[0][0]}

        return self.minPath(grid, r - 1, c - 1, cache)

    def minPath(self, grid, i, j, cache):
        key = (i, j)
        if key in cache:
            return cache[key]
        if i < 0 or j < 0:
            return math.inf
        cache[key] = min(self.minPath(grid, i - 1, j, cache),
                         self.minPath(grid, i, j - 1, cache)) + grid[i][j]
        return cache[key]

    # using caching to sole problem f time out
    # https://leetcode.com/problems/minimum-path-sum/discuss/380979/Simply-Simple-Python-Solution-DP-and-Recursion-with-memoization-both


# @lc code=end
