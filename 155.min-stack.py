#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#
# https://leetcode.com/problems/min-stack/description/
#
# algorithms
# Easy (35.71%)
# Likes:    3010
# Dislikes: 294
# Total Accepted:    506.4K
# Total Submissions: 1.2M
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n' +
'[[],[-2],[0],[-3],[],[],[],[]]'
#
# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.
#
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
#
#
#
# Example 1:
#
#
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
#
# Output
# [null,null,null,null,-3,null,0,-2]
#
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
#
#
#
# Constraints:
#
#
# Methods pop, top and getMin operations will always be called on non-empty
# stacks.
#
#
#

# @lc code=start


class MinStack:

    def __init__(self, val: int = None, node=None):
        """
        initialize your data structure here.
        """
        self.val = val
        self.next = node
        self.min = None


    def push(self, x: int) -> None:
        ms = MinStack(x)

        # print(x)
        if self.min is None:
            # print('x is none')
            self.min = x
        elif x < self.min:
            self.min = x

        node = self

        while node.next:
            node = node.next

        node.next = ms


    def pop(self) -> None:
        node = self
        if node.next:
            m = node.next.val
            # print(m)

            # m = self.val
            while node.next.next:
                node = node.next
                # if node.val < m:
                #     m = node.val
                # print(node.val)
                if int(node.val) < int(m):
                    m = node.val
                    print(m)

            # if int(node.val) < int(m):
            #     m = node.val

            node.next = None
            self.min = m

        # donothig if it is empty stack

    def top(self) -> int:
        node = self
        while node.next:
            node = node.next
        return node.val

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
