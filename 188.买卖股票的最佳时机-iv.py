#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
# 1、动态规划
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices: return 0
        dp = [[[0,0] for _ in range(k+1)] for _ in range(len(prices))]
        for i in range(len(prices)):
            for k in range(k+1,0,-1):
                if i == 0:
                    dp[i][k][0] = 0
                    dp[i][k][1] = float('-inf')

                else:
                    dp[i][k][0] = max(dp[i-1][k][0],dp[i-1][k][1]+prices[i])
                    dp[i][k][1] = max(dp[i-1][k][1],dp[i-1][k-1][0]-prices[i])
        return dp[-1][-1][0]

# @lc code=end

