from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Approach 1 : dynamic programming
        # wrong!!!: cooldown , you can not buy at some day
        # DP[i] , prices[i]的股票价格，第i天买卖股票的累计最大利润是DP[i]
        # selled or cooldown
        # DP[i] = DP[i-1] if prices[i] <= prices[i-1]
        # DP[i] = DP[i-1] + prices[i] - prices[i-1] if prices[i] > prices[i-1]
        n = len(prices)
        DP = [0 for _ in range(0,n)]
        DP.append(0)
        for i in range(1,len(prices)):
            pre = prices[i - 1]
            cur = prices[i]
            if cur > pre:
                DP[i] = DP[i-1] + cur - pre
            else:
                DP[i] = DP[i-1]
            print(pre,cur,i,DP)
        return DP[n-1]
print(Solution().maxProfit([1,2,3,0,2]))

        # Approach 2 : Wrong !!! j的状态定义不合理
        # DP[i][j] , 已知prices[i]的股票价格，
        # j表示当天的操作状态，0卖出1买入/买入持有2冷冻期
        # 第i天买卖股票的最大利润是DP[i]
        # DP[i][0] = DP[i-1][1] + prices[i] - prices[i-1] ; if prices[i] > prices[i-1]
        # DP[i][0] = DP[i-1][0] if prices[i] <= prices[i-1]
        # DP[i][0] = MAX(DP[i-1][1] + prices[i] - prices[i-1],DP[i-1][0])
        # DP[i][1] = DP[i-1][2]
        # DP[i][2] = DP[i-1][0]

        # Approach 2 题解: 
        # DP[i][j] , 已知prices[i]的股票价格，
        # j表示当天的操作状态，0持有1不持有+冷冻2不持有+非冷冻
        # 第i天买卖股票的最大利润是DP[i]
        # 买入算负收益，卖家算正收益
        # DP[i][0] = max(DP[i-1][0],DP[i-1][2] - prices[i])
        # DP[i][1] = DP[i-1][0] + prices[i]
        # DP[i][2] = max(DP[i-1][2], DP[i-1][1])
        # 初始值
        # DP[0][0] = -prices[0]
        # DP[0][1] = 0
        # DP[i][0] = 0
