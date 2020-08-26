#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1、直接双指针，也可以去掉非数字字母后再双指针
        # l,r=0,len(s)-1
        # while l<r:
        #     while not s[l].isalnum() and l<r:
        #         l+=1
        #     while not s[r].isalnum() and l<r:
        #         r-=1
        #     if s[l].lower()!=s[r].lower():
        #         return False
        #     l+=1
        #     r-=1
        # return True

        # 2、直接处理
        s=[ch.lower() for ch in s if ch.isalnum()]
        return s==s[::-1]

# @lc code=end

