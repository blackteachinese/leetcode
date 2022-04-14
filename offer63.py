class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 只能买一次
        # Approach 1
        # DP[i][j][k]表示第i天买卖股票的最大收益，j表示股票状态,0不持有，1持有, k是交易次数0或1
        # DP[i][0][0] 不持有，完成0次交易 = 0
        # DP[i][0][1] 不持有，完成1次交易 = max(DP[i-1][1], DP[i-1][0][0] + prices[i])
        # DP[i][1][0] 持有，完成0次交易 = DP[0][0] - prices[i]
        # DP[i][i][1] 不可能 

        # Approach 2 里有只买一次的特性
        # DP[i]表示第i天买卖股票的最大收益
        # DP[i] = max(DP[i-1],prices[i]- min(prices[0:i-1])))
