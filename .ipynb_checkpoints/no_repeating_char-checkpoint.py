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
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        begin = 0
        end = 0
        temp_dict = {}
        ll = 0
        for i, e in enumerate(s):
            if e in temp_dict:
                begin = max(begin,temp_dict[e]+1)
                temp_dict[e] = i
            else:
                temp_dict[e] = i
            end = i
            l = end - begin + 1
            print(end,begin)
            if l > ll:
                ll = l
        return ll
