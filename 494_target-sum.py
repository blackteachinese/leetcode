from typing import List


class Solution:
    def findTargetSumWays1(self, nums: List[int], target: int) -> int:
        # Approach 1: brute force + 回溯 + recursive O(2^n)
        # Approach 2: dp O(n^2)
        # +和-号，01背包
        # 遍历时数组的位置不能变换顺序 => 01背包组合问题
        # dp[i][j] = 选择数量为i的nums的每一个元素，每个元素可以是正也可以是负,组成表达式结果为j的组合个数，i取值范围[0.len(nums)]
        # dp[i][j] = dp[i-1][j - nums[i]] + dp[i-1][j + nums[i]]
        # !!! wrong j + nums[i]会大于j,遍历范围很难写
        x,y=target+1,len(nums)+1
        dp = [[0] * x for _ in range(y)]
        # 初始化
        dp[0][0] = 1
        for i in range(1,y):
            for j in range(1,x):
                if j - nums[i - 1] >= 0:
                    dp[i][j] += dp[i-1][j - nums[i - 1]]
                if x > j + nums[i - 1]:
                    dp[i][j] += dp[i-1][j + nums[i - 1]]
            print(dp)
        return  dp[y-1][x-1]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Approach 2: dp O(n^2)
        # 修改思路：基于一个题目一个数学等式，简化状态定义
        # 因为数组元素是固定的，要求正数和-负数和=固定的目标值，可推导出
        # => 正数和或负数和的值是固定值
        # 公式推导逻辑
        # 设所有元素和为sum,负数和为neg,整数和为pos，目标值为target
        # sum - neg = pos
        # pos - neg = target
        # => pos = (sum + target) / 2  = 固定值
        # => neg = (sum - target) / 2  = 固定值
        # 因此可以转化为求pos或neg等于固定值的组合数
        # 下面以求neg组合数为例
        # dp[i][j] = 选择数量为i的nums的每一个元素，每个元素都取正数,组成的和结果为j，求所有的组合个数，i取值范围[0.len(nums)]
        # dp[i][j] = dp[i-1][j](不取nums[i]) + dp[i-1][j - nums[i]](取nums[i])

        # 边界处理
        # sum - target 必须能整除2
        v_sum = sum(nums)
        if (v_sum - target) % 2 != 0:
            return 0
        neg = int((v_sum - target) / 2)
        if neg < 0:
            return 0
        # neg 必须是非负整数
        x,y=neg+1,len(nums)+1
        dp = [[0] * x for _ in range(y)]
        # 初始化
        dp[0][0] = 1
        # print(neg,y)
        for i in range(1,len(nums)+1): # 从第一个元素开始递推
            num = nums[i - 1]
            for j in range(0,neg+1): # wrong!!! 背包体积要从0开始递推，总数为neg
                if j - num < 0:
                    dp[i][j] = dp[i-1][j]
                else :
                    # dp[i][j] = dp[i-1][j] + dp[i][j - num]
                    # wrong !!！ 取过一次nums[i]就不能再取了，所以是dp[i-1][j - num]，而不是dp[i][j - num]
                    dp[i][j] = dp[i-1][j] + dp[i-1][j - num]
            # print(dp)
        return  dp[y-1][neg]
nums, target = [1,1,1,1,1] ,3
# nums, target = [1] ,1
# nums, target = [1,0] ,1

print(Solution().findTargetSumWays(nums,target))