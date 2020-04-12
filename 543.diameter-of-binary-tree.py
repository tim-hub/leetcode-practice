#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#
# https://leetcode.com/problems/diameter-of-binary-tree/description/
#
# algorithms
# Easy (46.24%)
# Likes:    2565
# Dislikes: 161
# Total Accepted:    279K
# Total Submissions: 578.1K
# Testcase Example:  '[1,2,3,4,5]'
#
#
# Given a binary tree, you need to compute the length of the diameter of the
# tree. The diameter of a binary tree is the length of the longest path between
# any two nodes in a tree. This path may or may not pass through the root.
#
#
#
# Example:
# Given a binary tree
#
# ⁠         1
# ⁠        / \
# ⁠       2   3
# ⁠      / \
# ⁠     4   5
#
#
#
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
#
#
# Note:
# The length of path between two nodes is represented by the number of edges
# between them.
#
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        # https://leetcode.com/problems/diameter-of-binary-tree/discuss/574083/Python3-recursive-solution
        def fn(node):
            """Return length+1 and diameter rooted at node"""
            if not node:
                return (0, 0)
            l1, d1 = fn(node.left)
            l2, d2 = fn(node.right)
            return 1 + max(l1, l2), max(d1, d2, l1+l2)

        return fn(root)[1]

# @lc code=end


Solution().diameterOfBinaryTree()
