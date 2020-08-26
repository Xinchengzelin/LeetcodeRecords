#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 字符串处理-双指针
        # if x<0:
        #     return False
        # else:
        #     s=str(x)
        #     l,r=0,len(s)-1
        #     while l<r:
        #         if s[l]==s[r]:
        #             l+=1
        #             r-=1
        #         else:
        #             return False
        # return True
        # 字符串直接处理
        # s=str(x)
        # return s==s[::-1]

        # 3、数学的方法
        if x<0 or (x%10==0 and x!=0):
            return False
        revertednum=0
        while x>revertednum:
            revertednum=revertednum*10+x%10
            x=x//10
        return x==revertednum or x==revertednum//10

# @lc code=end

