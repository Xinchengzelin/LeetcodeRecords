#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
# 1、哈希表
# class Solution:
#     def wordPattern(self, pattern: str, s: str) -> bool:
#         if len(pattern) != len(list(s.split())):
#             return False
#         dic = {}
#         for p,s in zip(pattern,s.split()):
#             if p in dic.keys():
#                 if dic[p] != s:
#                     return False
#             else:
#                 if s in dic.values():#此处逻辑易漏
#                     return False
#                 else:
#                     dic[p] = s
#         return True

# 2、利用map
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p = pattern
        t = s.split()
        return list(map(p.find,p))==list(map(t.index,t))
  
# @lc code=end

