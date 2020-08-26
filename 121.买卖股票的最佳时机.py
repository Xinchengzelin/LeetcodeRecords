#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
# 1、动态规划 15.51%/5.03%
# dp[i][k][0 or 1]
# class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     if not prices: return 0
    #     dp = [[0,0] for _ in range(len(prices))]
    #     for i in range(len(prices)):
    #         if i == 0:
    #             dp[i][0] = 0
    #             dp[i][1] = -prices[i]
    #         else:
    #             dp[i][0] = max(dp[i-1][1] + prices[i], dp[i-1][0])
    #             dp[i][1] = max(dp[i-1][1], -prices[i])# 只有1次，不是dp[i-1][0] - prices[i]
    #     print(dp)
    #     return dp[-1][0]
# 2、动态规划-减小空间复杂度 41.66%/84.92%
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices: return 0
#         dp_i_0, dp_i_1 = 0, float("-inf")
#         for i in range(len(prices)):
#             if i == 0:
#                 dp_i_1 = -prices[i]
#             else:
#                 dp_i_0 = max(dp_i_0,dp_i_1+prices[i])
#                 dp_i_1 = max(dp_i_1, -prices[i])
#         return dp_i_0
# 3、直接计算 59.38%/94%
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice,maxprofit)
            minprice = min(minprice,price)
        return maxprofit

# @lc code=end

