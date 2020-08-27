#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
# 1、动态规划  5.14%/5.1%
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices: return 0
#         dp = [[[0,0] for _ in range(3)] for _ in range(len(prices))]
#         for i in range(len(prices)):
#             for k in range(2,0,-1):
#                 if i == 0:
#                     dp[i][k][0] = 0
#                     dp[i][k][1] = -prices[i] #注意不是-inf
#                 else:
#                     dp[i][k][0] = max(dp[i-1][k][0],dp[i-1][k][1]+prices[i])
#                     dp[i][k][1] = max(dp[i-1][k][1],dp[i-1][k-1][0]-prices[i])
#         return dp[-1][-1][0]
# 1、动态规划-优化空间  5.14%/5.1%
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        dp_i10 = 
        dp_i11 =
        dp_i20 =
        dp_i21 =
        for i in range(len(prices)):


# @lc code=end

