#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I":1,"V" :5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        if len(s)==1:
            return dic[s]
        res = 0
        for i in range(len(s)-1):
            if dic[s[i]] < dic[s[i+1]]:
                res -= dic[s[i]]
            else:
                res += dic[s[i]]
        return res+dic[s[-1]]
# @lc code=end

