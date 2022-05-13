from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # Approach 1 : dynamic programming
        # 无冷冻期，有交易费用
        # DP[i][j]表示第i天买卖股票的最大收益，j表示股票状态,0不持有，1持有
        # DP[i][0] = max(DP[i-1][0],DP[i-1][1]+prices[i]-fee)
        # DP[i][1] = max(DP[i-1][1],DP[i-1][0]-prices[i])