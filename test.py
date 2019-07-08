# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.1.7
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp_dict = {}
        for i, x in enumerate(nums):
            if x not in temp_dict:
                temp_dict[x] = i
            y = target - x
            if y in temp_dict and temp_dict[y] != i:
                return [temp_dict[y],i]


# %%
s = Solution()
s.twoSum([3,3],6)
print(s.twoSum([3,2,3,3],6))
