#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#
# https://leetcode.com/problems/valid-parenthesis-string/description/
#
# algorithms
# Medium (32.13%)
# Likes:    1390
# Dislikes: 43
# Total Accepted:    77.2K
# Total Submissions: 245.7K
# Testcase Example:  '"()"'
#
#
# Given a string containing only three types of characters: '(', ')' and '*',
# write a function to check whether this string is valid. We define the
# validity of a string by these rules:
#
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left
# parenthesis '(' or an empty string.
# An empty string is also valid.
#
#
#
# Example 1:
#
# Input: "()"
# Output: True
#
#
#
# Example 2:
#
# Input: "(*)"
# Output: True
#
#
#
# Example 3:
#
# Input: "(*))"
# Output: True
#
#
#
# Note:
#
# The string size will be in the range [1, 100].
#
#
#

# @lc code=start


class Solution:
    def checkValidString(self, s: str) -> bool:
        if len(s) == 0 or s == '*':
            return True
        if len(s) == 1:
            return False

        leftBalance = 0
        # from left
        for i in s:
            if i == ')':
                leftBalance -= 1
            else:
                leftBalance += 1

            if leftBalance < 0:
                # If number of ) brackets is more than the sum of ( and *, string is unbalanced
                return False

        if leftBalance == 0:
            return True

        rightBalance = 0
        # from right
        for i in reversed(s):
            if i == '(':
                rightBalance -= 1
            else:
                rightBalance += 1

            if rightBalance < 0:
                # If number of ( brackets is more than the sum of ) and *, string is unbalanced
                return False

        return True


# @lc code=end

print(Solution().checkValidString(
    "*()(())*()(()()((()(()()*)(*(())((((((((()*)(()(*)"))


# https://leetcode.com/problems/valid-parenthesis-string/discuss/577216/Python-Easy-O(N)-time-and-O(1)-space
