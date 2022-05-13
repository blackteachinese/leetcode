from typing import List

class Solution:
    def coinChange1(self, coins: List[int], amount: int) -> int:
        # 背包问题：总面额=背包体积，不同面额硬币=不同体积的物品，每个硬币的价值一样，可以认为都是1
        # 完全背包问题: 每种硬币都可以取多次
        # 完全背包最值问题：求硬币数量最少的解，相当于求最小值

        # Approach 1: 二维 O(n*amount^2) n=len(coins)
        # DP[i][j]表示任意使用i种硬币，组成面额为j，所用的最少的硬币数量是多少
        # DP[i][j]可拆分为两种情况，1不使用第i种硬币时硬币数量最少的解，2使用第i种硬币时硬币数量最少的解
        # 不使用第i种硬币时硬币数量最少的解 = DP[i-1][j]
        # 使用第i种硬币时硬币数量最少的解 = DP[i-1][j-coins[i]]+1 ,...DP[i-1][j-k*coins[i]]+k ;其中k*coins[i] <= amount
        # DP[i][j] = min(DP[i-1][j], DP[i-1][j-k*coins[i]]+k {k取值范围[1:amount//coins[i]]})
        # 初始值
        # dp[i][0] = 0 凑成总面额为0的最少硬币个数是0个，
        # 其他情况无法判断方案，统一设为最大值 float('inf')
    
        x,y=len(coins)+1,amount + 1
        dp =[[float('inf')] * y for _ in range(0,x) ]
        # 初始值
        for i in range(0,x):
            dp[i][0] = 0
        for i in range(1,x):
            for j in range(0,y):
                for k in range(0,amount//coins[i-1] + 1):
                    # print(dp[i-1][j-k*coins[i]] + k)
                    dp[i][j] = min(dp[i][j], dp[i-1][j-k*coins[i-1]] + k)
        return dp[x-1][y-1] if dp[x-1][y-1] != float('inf') else -1


    def coinChange2(self, coins: List[int], amount: int) -> int:
        # Approach 2: 优化    O(n*amount) n=len(coins)
        # 使用第i种硬币总面额达amount时硬币数量最少的解 = 任意使用硬币总面额达(amount-coins[i])时硬币数量最少的解+1（使用1次第i种硬币）
        # DP[i-1][j-k*coins[i]]+k {k取值范围[1:amount//coins[i]]})
        #  = DP[i][j-coins[i]] + 1
        x,y=len(coins)+1,amount+1
        dp=[[float('inf')] * y for _ in range(0,x)]
        # initial
        for i in range(0,x):
            dp[i][0] = 0
        # print(dp)
        for i in range(1,x):
            for j in range(0,y):
                if j-coins[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    # print(i,j,j-coins[i-1])
                    dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i-1]] + 1)
        return dp[len(coins)][amount] if dp[len(coins)][amount] != float('inf') else -1


    def coinChange(self, coins: List[int], amount: int) -> int:
        # Approach 3: 去掉一维 O(n*amount) n=len(coins)
        # 优化前：dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i-1]] + 1)
        # dp[j] 表示任意使用i种硬币，组成面额为j，所用的最少的硬币数量
        # dp[j] = min{第1种硬币至少用一次时，... 第i种硬币至少用一次时}
        # dp[j] = min(dp[j - coins[0]] + 1,...,dp[j - coins[i]] + 1);

        y=amount+1
        dp=[float('inf')] * y
        # initial
        dp[0] = 0
        # print(dp)
        for j in range(1,y):
            for i in range(0,len(coins)):
                # print(j-coins[i-1])
                if j-coins[i] < 0:
                    continue
                dp[j] = min(dp[j], dp[j-coins[i]] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

# coins,amount = [1, 2, 5], 11
# coins,amount = [2], 3
# coins,amount = [1], 0
# coins,amount = [3,7,405,436],8839 # 二维会超出时间限制
# coins,amount = [1,2147483647],2
# print(Solution().coinChange(coins,amount))