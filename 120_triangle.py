from typing import List


class Solution:
    def minimumTotal1(self, triangle: List[List[int]]) -> int:
        # Approach 1: brute force 递归搜索+回缩 O(n!) n代表行数
        # Approach 2: dp 自顶向下遍历的思路
        # dp[i][j] 以第i行，第j列元素结尾的最短路径和
        # 从左到右，从上到下遍历，i从0到len(triangle),j从0到len(triangle[i])
        # 第一行作为初始值，不用计算
        # dp[i][j] = min(dp[i-1][j] , dp[i-1][j-1]) + triangle[i][j] if j >= 1
        # dp[i][j] = dp[i-1][j] + triangle[i][j]) if j == 0，因为j==0时，上一行j-1的位置不存在
        # dp[i][j] = dp[i-1][j-1]+ triangle[i][j]) if j == i ，因为j==i时，上一行j==i的位置不存在
        # res = min(dp[i][0],...,dp[i][triangle[-1]])
        dp=triangle
        for i in range(1,len(triangle)):
            for j in range(0,len(triangle[i])):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == i:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j] , dp[i-1][j-1]) + triangle[i][j]
        return min(dp[len(triangle)-1])

        # Approach 2: dp 自低向上遍历的思路
        # 代码逻辑会比较简单，不用考虑特殊情况
        # 从下到上，从右到左，i从len(triangle)到0,j从len(triangle[i])到0
        # 最后一行作为初始值，不用计算
        # dp[i][j] = min(dp[i+1][j],dp[i+1][j+1]) + triangle[i][j]
        # res = d[0][0]  第一行只有一个元素

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        mini = triangle # 拷贝triangle的数值，最后一行初始值作为递推基础
        for i in range(len(triangle) - 2, -1, -1): #自底向上遍历每一行
            for j in range(0,len(triangle[i]),1):
                # 动态规划的状态转移方程
                mini[i][j] = min(mini[i+1][j], mini[i+1][j+1]) + triangle[i][j]
        return mini[0][0]
        
# triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# triangle = [[-10]]
# print(Solution().minimumTotal(triangle))