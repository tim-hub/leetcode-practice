#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (44.84%)
# Likes:    2993
# Dislikes: 166
# Total Accepted:    596.5K
# Total Submissions: 1.1M
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings, group anagrams together.
#
# Example:
#
#
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
#
# Note:
#
#
# All inputs will be in lowercase.
# The order of your output does not matter.
#
#
#

# @lc code=start
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r = {}
        for s in strs:
            the_set = ''.join(sorted(s))
            if the_set in r:
                r[the_set].append(s)
            else:
                r[the_set] = [s]
        # print(list(map(lambda x: x[1], r.items())))
        return list(map(lambda x: x[1], r.items()))

# @lc code=end


# Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])


test2 = ["hos", "boo", "nay", "deb", "wow", "bop", "bob", "brr", "hey", "rye", "eve", "elf", "pup", "bum", "iva", "lyx", "yap", "ugh", "hem", "rod", "aha", "nam",
         "gap", "yea", "doc", "pen", "job", "dis", "max", "oho", "jed", "lye", "ram", "pup", "qua", "ugh", "mir", "nap", "deb", "hog", "let", "gym", "bye", "lon", "aft", "eel", "sol", "jab"]

exp2 = [["sol"], ["wow"], ["gap"], ["hem"], ["yap"], ["bum"], ["ugh", "ugh"], ["aha"], ["jab"], ["eve"], ["bop"], ["lyx"], ["jed"], ["iva"], ["rod"], ["boo"], ["brr"], ["hog"], ["nay"], ["mir"], ["deb", "deb"], ["aft"], [
    "dis"], ["yea"], ["hos"], ["rye"], ["hey"], ["doc"], ["bob"], ["eel"], ["pen"], ["job"], ["max"], ["oho"], ["lye"], ["ram"], ["nap"], ["elf"], ["qua"], ["pup", "pup"], ["let"], ["gym"], ["nam"], ["bye"], ["lon"]]

r = Solution().groupAnagrams(['bob', 'boo'])
