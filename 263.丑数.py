#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#

# @lc code=start
class Solution:
    def isUgly(self, num: int) -> bool:
        # 1、直接法，依次除2/3/5,结果为1，则是丑数
        if num<=0:
            return False
        for i in [2,3,5]:
            while num%i==0:
                num/=i
        return num==1

# @lc code=end

