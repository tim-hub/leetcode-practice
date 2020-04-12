from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        remaining = stones

        while len(remaining) > 1:
            s = sorted(remaining)
            top_two = s[-2:]

            smashed = top_two[1]-top_two[0]

            if smashed > 0:
                remaining = s[:-2]+[smashed]
            else:
                remaining = s[:-2]

        return 0 if len(remaining) < 1 else remaining[0]


t = [2, 7, 4, 1, 8, 1]
r = Solution().lastStoneWeight(t)

print(r)
