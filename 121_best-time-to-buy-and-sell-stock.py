from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 题目：股票买卖一次
        # Approach 1 : dynamic programming
        # DP[i][j]表示第i天股票买卖累计收益最大值,j表示股票状态，0持有，1不持有
        # !!!Wrong 忽略了题目条件，股票买卖一次 DP[i][0] = max(DP[i-1][0],DP[i-1][1] - prices[i])
        # DP[i][0] = max(DP[i-1][0], - prices[i])
        # DP[i][1] = max(DP[i-1][1],DP[i-1][0] + prices[i]) 
        