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
# 2、动态规划-优化空间  5.04%/28.51%
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices: return 0
#         dp_i10 = 0
#         dp_i11 = float('-inf')#-prices[0]
#         dp_i20 = 0
#         dp_i21 = float('-inf')
#         for i in range(len(prices)):
#             dp_i20 = max(dp_i20,dp_i21+prices[i])
#             dp_i21 = max(dp_i21,dp_i10-prices[i])
#             dp_i10 = max(dp_i10,dp_i11+prices[i])
#             dp_i11 = max(dp_i11,-prices[i])
#         return dp_i20
#  2.1、动态规划-和上面一样  5.04%/28.51%
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        dp_i10 = 0
        dp_i11 = -prices[0]
        dp_i20 = 0
        dp_i21 = float('-inf')#-prices[0] 这两个都可以
        for i in range(len(prices)):
            dp_i20 = max(dp_i20,dp_i21+prices[i])
            dp_i21 = max(dp_i21,dp_i10-prices[i])
            dp_i10 = max(dp_i10,dp_i11+prices[i])
            dp_i11 = max(dp_i11,-prices[i])
        return dp_i20


# @lc code=end

