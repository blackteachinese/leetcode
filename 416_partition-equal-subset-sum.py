from typing import List


class Solution:
    def canPartition1(self, nums: List[int]) -> bool:
        # Approach 1 : dP 自己分析
        # DP[i][j] 元素个数为i数组nums中是否能分割出一个子集，子集元素和为j，j取nums数组元素和的1/2
        # !!!Wrong 不一定要选取nums[i],可以拆分为选择和情况和不选取的情况
        # DP[i][j] =(选取) DP[i-1][j-nums[i]](if j-nums[i] >= 0 ) or DP[i-1][2*j-nums[i]](if j-nums[i] < 0 )
        sum_nums = sum(nums)
        if sum_nums & 1:
            return False
        half = sum_nums >> 2
        x = len(nums)+1
        y = half + 1
        dp = [[False] * y for _ in range(0,x)]
        dp[0][0] = True
        print(dp)
        for i in range(0,x):
            for j in range(0,y):
                if 2*j <= nums[i - 1]:
                    dp[i][j] = False
                elif j <= nums[i - 1]:
                    dp[i][j] = dp[i-1][2*j - nums[i - 1]]
                else :
                    dp[i][j] = dp[i-1][j - nums[i - 1]]
        return dp[x-1][y-1]

    def canPartition2(self, nums: List[int]) -> bool:
        # Approach 1 : dP 状态递推方程修正
        # DP[i][j] 元素个数为i+1个的数组nums中是否能分割出一个子集，子集元素和为j，j取nums数组元素和的1/2
        # !!! 不一定要选取nums[i],可以拆分为选择和情况和不选取的情况
        # DP[i][j] = (选取i)DP[i-1][j-nums[i]] or (不选取i)DP[i-1][j]
        ## if j < nums[i]: dp[i][j] = dp[i-1][j]
        ## elif j = nums[i]: dp[i][j] = True
        ## elif j > nums[i]: dp[i-1][j - nums[i]] or dp[i-1][j]
        # 初始化 ！！！重要
        #  j == nums[i]: dp[i][j] = True
        sum_nums = sum(nums)
        if sum_nums & 1:
            return False
        half = sum_nums >> 1 # !!! wrong 一开始写成 sum_nums>>2
        x = len(nums) # !!! wrong len(nums)不用+1了，否则会难以理解
        y = half + 1
        dp = [[False] * y for _ in range(0,x)]
        # 初始化
        # dp[0]代表只可选取num[0]，如果j=num[0]则必定成立
        # dp[0][nums[0]] = True
        # ！！！wrong,i和j如果从0开始会有case错误，i和j都应该从1开始
        for i in range(1,x):
            for j in range(1,y):
                if j < nums[i]:
                    dp[i][j] = dp[i-1][j]
                elif j == nums[i]:
                    dp[i][j] = True
                else :
                    dp[i][j] = dp[i-1][j - nums[i]] or dp[i-1][j]
        return dp[x-1][y-1]

    def canPartition(self, nums: List[int]) -> bool:
        # Approach 1 : dP 使用题解的初始化条件
        # DP[i][j] 元素个数为i+1个的数组nums中是否能分割出一个子集，子集元素和为j，j取nums数组元素和的1/2
        # !!! 不一定要选取nums[i],可以拆分为选择和情况和不选取的情况
        # DP[i][j] = (选取i)DP[i-1][j-nums[i]] or (不选取i)DP[i-1][j]
        ## if j < nums[i]: dp[i][j] = dp[i-1][j]
        ## elif j > nums[i]: dp[i-1][j - nums[i]] or dp[i-1][j]
        
        # 放弃：elif j = nums[i]: dp[i][j] = True
        # 使用：如果不选取任何正整数，则被选取的正整数等于0。因此对于所有0<=i<n,都有dp[i][0] = true

        sum_nums = sum(nums)
        if sum_nums & 1:
            return False
        half = sum_nums >> 1 # !!! wrong 一开始写成 sum_nums>>2
        x = len(nums) # !!! wrong len(nums)不用+1了，否则会难以理解
        y = half + 1
        dp = [[False] * y for _ in range(0,x)]
        # 初始化
        # dp[0]代表只可选取num[0]，如果j=num[0]则必定成立
        for i in range(x):
            dp[i][0] = True
        # dp[0][nums[0]] = True
        # ！！！wrong,i和j如果从0开始会有case错误，i和j都应该从1开始
        for i in range(1,x):
            for j in range(1,y):
                if j < nums[i]:
                    dp[i][j] = dp[i-1][j]
                # elif j == nums[i]:
                #     dp[i][j] = True
                else :
                    dp[i][j] = dp[i-1][j - nums[i]] or dp[i-1][j]
        return dp[x-1][y-1]

# nums = [1,5,11,5]
# nums = [1,1]
nums = [1,2,3,5]
# nums = [4,4,4,4,4,4,4,4,8,8,8,8,8,8,8,8,12,12,12,12,12,12,12,12,16,16,16,16,16,16,16,16,20,20,20,20,20,20,20,20,24,24,24,24,24,24,24,24,28,28,28,28,28,28,28,28,32,32,32,32,32,32,32,32,36,36,36,36,36,36,36,36,40,40,40,40,40,40,40,40,44,44,44,44,44,44,44,44,48,48,48,48,48,48,48,48,52,52,52,52,52,52,52,52,56,56,56,56,56,56,56,56,60,60,60,60,60,60,60,60,64,64,64,64,64,64,64,64,68,68,68,68,68,68,68,68,72,72,72,72,72,72,72,72,76,76,76,76,76,76,76,76,80,80,80,80,80,80,80,80,84,84,84,84,84,84,84,84,88,88,88,88,88,88,88,88,92,92,92,92,92,92,92,92,96,96,96,96,96,96,96,96,97,99]
print(Solution().canPartition(nums))