class Solution:
    def maxProfit(self, prices: List[int]) -> int:
# 只能买卖两次，没有冷冻期
# DP[i][j][k], 表示第i天，完成不超过2笔交易后，累计收益最大值.
# j表示股票状态，0不持有、1持有,k表示完成交易数，取值范围0，1，2；

# DP[i][0][0] （不持有，完成0次交易） = 0
# DP[i][1][0] （持有，完成0次交易） = max(DP[i-1][1][0],-prices[i-1])
# DP[i][0][1] （不持有，完成1次交易） = max(DP[i-1][0][1],DP[i-1][1][0] + prices[i])
# DP[i][1][1] （持有，完成1次交易） = max(DP[i-1][1][1],DP[i-1][0][1]-prices[i] )
# DP[i][0][2] （不持有，完成2次交易）= max(DP[i-1][1][1] + prices[i], DP[i-1][0][2])


# DP[i][1] = DP[i-1][1],DP[i-1][0] + prices[i]
