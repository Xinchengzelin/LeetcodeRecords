#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
# 1、动态规划 56.27%/32.02%
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices: return 0
#         dp = [[0,0] for _ in range(len(prices))]
#         for i in range(len(prices)):
#             if i == 0:
#                 dp[i][0] = 0
#                 dp[i][1] = -prices[i]
#             elif i == 1:
#                 dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
#                 dp[i][1] = max(dp[i-1][1], -prices[i])

#             else:
#                 dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
#                 dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i])
#         return dp[-1][0]
# 2、动态规划-节约空间 90.14%/99.68%
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        dp_i_0,dp_i_1 = 0, -prices[0]
        dp_pre = 0 #代表dp[i-2][0]
        for i in range(len(prices)):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0,dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1,dp_pre - prices[i])
            dp_pre = temp
        return dp_i_0

# @lc code=end

