#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start

# 1、贪心 84.95%/80.33%
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         res=0
#         for i in range(1,len(prices)):
#             if prices[i]>prices[i-1]:
#                 res+=prices[i]-prices[i-1]
#         return res

# 2、动态规划-24.51%/7.98%
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices: return 0
#         dp = [[0,0] for _ in range(len(prices))]
#         for i in range(len(prices)):
#             if i == 0:
#                 dp[i][0] = 0
#                 dp[i][1] = -prices[i]#float('-inf')
#             else:
#                 dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
#                 dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
#         return dp[-1][0]
# 3、动态规划-减少空间 39.01%/38.91%
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        dp_i_0,dp_i_1 = 0,-prices[0]
        for i in range(1,len(prices)):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0,dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1,dp_i_0 - prices[i])
        return dp_i_0
# @lc code=end

