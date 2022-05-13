class Solution:
    def climbStairs(self, n: int) -> int:
        # Approach 1 : 
        # 无后效性 ok
        # DP[i], 爬到第i阶楼梯的方法总数
        # DP[i] = DP[i-1] + DP[i-2]
        # space optimize roll array