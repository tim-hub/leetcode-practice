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
        # depth first
        def gotoRight(subGrid: List[List[int]]) -> List[List[int]]:
            return list(map(lambda g: g[1:], subGrid))

        def gotoDown(subGrid: List[List[int]]) -> List[List[int]]:
            return subGrid[1:]

        def findMin(subGrid: List[List[int]]) -> int:
            # print(subGrid)
            if (len(subGrid) == 1 and len(subGrid[0]) == 1):
                return subGrid[0][0]

            if (len(subGrid) == 1):
                return subGrid[0][0]+findMin(gotoRight(subGrid))
            if (len(subGrid[0]) == 1):
                return subGrid[0][0]+findMin(gotoDown(subGrid))

            r = min(
                subGrid[0][0]+findMin(gotoRight(subGrid)),
                subGrid[0][0]+findMin(gotoDown(subGrid))
            )
            # print(r)
            return r

        return findMin(grid)


# @lc code=end
