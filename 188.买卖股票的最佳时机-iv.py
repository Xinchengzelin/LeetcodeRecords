#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
# 1、动态规划 61.44%/55.08%
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices: return 0
        if k > (len(prices)>>1): return self.maxProfit_kinf(prices)
        dp = [[[0,0] for _ in range(k+1)] for _ in range(len(prices))]
        for i in range(len(prices)):
            for j in range(k,0,-1):
                if i == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[i] #注意不是-inf
                else:
                    dp[i][j][0] = max(dp[i-1][j][0],dp[i-1][j][1]+prices[i])
                    dp[i][j][1] = max(dp[i-1][j][1],dp[i-1][j-1][0]-prices[i])
        return dp[-1][-1][0]
    def maxProfit_kinf(self, prices: List[int]) -> int:
        res=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                res+=prices[i]-prices[i-1]
        return res

# @lc code=end

