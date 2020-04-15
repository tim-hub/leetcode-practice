class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:

        def to_shift(s: str, direction: int, amount: int):

            l = len(s)
            if amount > l:
                amount = amount % l
            if amount == l or amount == 0:
                return s

            if direction == 0:
                return s[amount:] + s[:amount]
            else:
                return s[-amount:] + s[:l-amount]

        left_count = 0
        right_count = 0
        for sh in shift:
            if sh[0] == 0:
                left_count += sh[1]
            else:
                right_count += sh[1]
        final_amount = left_count - right_count

        direction = 0 if final_amount > 0 else 1
        the_amount = final_amount if final_amount > 0 else -final_amount
        # print(direction, the_amount)
        return to_shift(s, direction, the_amount)
