#
# @lc app=leetcode.cn id=779 lang=python3
#
# [779] 第K个语法符号
#

# @lc code=start
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        def helper(N,K,S,level):
            if level == N:
                return S[K-1]
            for i in S:
                
        S = ""
        return helper(N,K,S,0)



        
# @lc code=end

