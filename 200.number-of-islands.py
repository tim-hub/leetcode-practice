#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (40.33%)
# Likes:    4696
# Dislikes: 178
# Total Accepted:    623.2K
# Total Submissions: 1.4M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
#
# Example 1:
#
#
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1
#
#
# Example 2:
#
#
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3
#
#
from collections import deque
# @lc code=start


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        count = 0
        check = [[False for _ in range(len(grid[0]))]
                 for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and check[i][j] == False:
                    count += 1
                    self.search(grid, check, i, j)
        return count

    def search(self, grid, check, i, j):
        qu = deque([(i, j)])
        while qu:
            i, j = qu.popleft()
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1' and check[i][j] == False:
                check[i][j] = True
                qu.extend([(i-1, j), (i+1, j), (i, j-1), (i, j+1)])

# @lc code=end

# https://leetcode.com/problems/number-of-islands/discuss/345981/Python3Number-of-Islands-BFS-%2B-DFS
