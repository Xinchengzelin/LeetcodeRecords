#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
# 1、动态规划 35.64%/22.43%
# class Solution:
#     def maxProfit(self, prices: List[int], fee: int) -> int:
#         if not prices: return 0
#         dp = [[0,0] for _ in range(len(prices))]
#         for i in range(len(prices)):
#             if i == 0:
#                 dp[i][0] = 0
#                 dp[i][1] = -prices[i]-fee
#             else:
#                 dp[i][0] = max(dp[i-1][0],dp[i-1][1] + prices[i])
#                 dp[i][1] = max(dp[i-1][1],dp[i-1][0] - prices[i] - fee)
#         return dp[-1][0]
# 2、动态规划-精简空间 85.97%/52%
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices: return 0
        dp_i_0,dp_i_1 = 0, -prices[0]-fee
        for i in range(len(prices)):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0,dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1,temp -prices[i]-fee)
        return dp_i_0

# @lc code=end

