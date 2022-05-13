from typing import List

class Solution:
    def change1(self, amount: int, coins: List[int]) -> int:
        # Approach 1 : DP  完全背包不考虑顺序的组合问题
        # dp[i][j] 在i个数组中任意选择硬币，组成总面额为j的组合个数
        # dp[i][j] = 不选取coin[i]的组合数+选取coin[i]的组合数
        # dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]  if j >= coins[i]
        # dp[i][j] = dp[i-1][j]  if j < coins[i]
        # 初始值，组合问题，需要思考哪些场景一定只有1种组合
        x,y=len(coins),amount+1
        dp = [[0]*y for _ in range(x)]
        # 初始化y==0的情况
        # y==0表示，目标总面额为0，此时无论有多少种硬币，都只能一个都不选，只有1种组合
        for i in range(x): 
            dp[i][0] = 1
        # 初始化x==0的情况
        # x==0表示只能选取第一个元素coins[0]，如果目标总面额是coins[0]的倍数，此时组合数只有1种
        for j in range(1,y):
            v = coins[0]
            if (j % v) == 0:
                dp[0][j] = 1
        # print(dp)
        # 递推公式
        for i in range(1,x): # 从1开始，因为递推要求i-1，i需要>=1
            for j in range(1,y):# 从1开始，0已经初始化过了
                if j < coins[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]
        # print(dp)
        return dp[x-1][amount]

    def change2(self, amount: int, coins: List[int]) -> int:
        # Approach 2 : DP 修改递推边界，简化初始化逻辑
        # 修改前：硬币取值范围[1:len(coins)]
        # 修改前：硬币取值范围[0:len(coins)], 可取硬币为0时初始化条件比较简单
        x,y=len(coins)+1,amount+1
        dp = [[0]*y for _ in range(x)]
        # 初始化y==0的情况
        for i in range(x): 
            dp[i][0] = 1
        # 初始化x==0的情况,可取硬币为0时初始化条件比较简单
        dp[0][0] = 1
        # 递推公式
        # coins[i] => coins[i-1]
        for i in range(1,x):
            for j in range(1,y):
                if j < coins[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
        return dp[x-1][amount]

    def change3(self, amount: int, coins: List[int]) -> int:
        # Approach 2 : DP 修正x,y轴错误
        y,x=len(coins)+1,amount+1
        dp = [[0]*x for _ in range(y)]
        print(dp)
        print('x:',len(dp),'y:',len(dp[0]))
        # 初始化y==0的情况
        for i in range(y): 
            dp[i][0] = 1
        # 初始化x==0的情况,可取硬币为0时初始化条件比较简单
        dp[0][0] = 1
        # 递推公式
        for i in range(1,y):
            for j in range(1,x):
                if j < coins[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
        return dp[y-1][amount]


    def change(self, amount: int, coins: List[int]) -> int:
        # Approach 3 : DP 降维，去掉物品选择的维度
        # 修改前递推公式
        # dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]  if j >= coins[i]
        # dp[i][j] = dp[i-1][j]  if j < coins[i]

        # 降维推导逻辑
        # case:amount,coins = 5,[1, 2, 5]
       
        # 如果求组合数就是外层for循环遍历物品，内层for遍历背包。
        # 如果求排列数就是外层for遍历背包，内层for循环遍历物品。


        x=amount+1
        dp = [0]*x
        # 初始化x==0的情况
        dp[0] = 1
        # 注意！！！因为滚动数据压缩后，只保留上一行或上一列的数据，而dp[i][j-coins[i-1]] 代表同一行的左方，但具体是那一列不确定，所以此题不能一列一列遍历，只能一行一行遍历
        for i in range(len(coins)):
            coin = coins[i]
            for j in range(coin,x): # j < coin会越界，不计算
                dp[j] += dp[j - coin]
        return dp[amount]



amount,coins = 5,[1, 2, 5]

# amount,coins = 3,[2]


#矩阵展开，x轴是总面额（背包体积），y轴是硬币（物品)
# * 1,2,3,4,5
# 1
# 2
# 3
# 根据二维递推公式 dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]，可知某个矩阵位置是又其位置的上方和左方的矩阵位置推导而来
# dp[i][j] = dp[i-1][j]（正上方一格） + dp[i][j-coins[i-1]]（同一行的左方，具体是那一列不确定）
# 因此推导矩阵位置的值，实际上只需要用到i-1行的数据，和当前列j的前面几列的数据，所以i-2行及之前的数据都可以被覆盖，因此可以用滚动数组优化，第i行的计算结果直接覆盖第i-1行的数据，实现降维。
# dp[j] = dp[j] + dp[j-coins[i-1]]
# 注意！！！因为滚动数据压缩后，只保留上一行或上一列的数据，而dp[i][j-coins[i-1]] 代表同一行的左方，但具体是那一列不确定，所以此题不能一列一列遍历，只能一行一行遍历
       
# amount,coins = 10,[10]
# print(Solution().change3(amount,coins))


# 详细解读
# https://programmercarl.com/0518.%E9%9B%B6%E9%92%B1%E5%85%91%E6%8D%A2II.html