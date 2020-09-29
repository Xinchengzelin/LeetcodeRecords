#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#

# @lc code=start
# 1、异或
# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#         s = s+t
#         res = ord(s[0])
#         for i in range(1,len(s)):
#             res = res ^ ord(s[i])
#         return chr(res)

# 2、哈希表
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic = {}
        for ch in s:
            dic[ch] = dic.get(ch,0)+1
        for ch in t:
            if dic.get(ch,0) == 0:
                return ch
            else:
                dic[ch] -= 1


# @lc code=end

