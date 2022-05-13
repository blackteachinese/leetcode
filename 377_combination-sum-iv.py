from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Approach 1: 完全背包排列问题（考虑顺序的组合问题）
        # caes: nums,target = [1,2,3],4
        # 矩阵展开，x轴是target,y轴是nums
        # * 1,2,3,4
        # 1
        # 2
        # 3
        # 二维dp定义
        # dp[i][j],i是nums,j是target,dp[y][x]
        # 任意选取[0,y]的数组元素，组成总数位j的组合个数
        # 递推公式：拆分为取第i个数和不取第i个数两种情况
        # dp[i][j] = dp[i-1][j] + dp[i][j-nums[i]]

        # 降一维
        # dp[j] = dp[j] + dp[j-nums[i]]
        # 遍历顺序
# 如果求组合数就是外层for循环遍历物品，内层for遍历背包。
# 如果求排列数就是外层for遍历背包，内层for循环遍历物品。
# 如果把遍历nums（物品）放在外循环，遍历target的作为内循环的话，举一个例子：计算dp[4]的时候，结果集只有 {1,3} 这样的集合，不会有{3,1}这样的集合，因为nums遍历放在外层，3只能出现在1后面！
# 所以本题遍历顺序最终遍历顺序：target（背包）放在外循环，将nums（物品）放在内循环，内循环从前到后遍历。
        x,y =  target + 1,len(nums)
        dp = [0] * x
        # 初始化
        dp[0] = 1
        # 排列问题，先遍历背包(总数)
        for j in range(1,x): # 先遍历背包(总数)
            for i in range(0,y): # 遍历物品要从第1个开始取，i从0开始
                if j - nums[i] >= 0:
                    dp[j] = dp[j] + dp[j - nums[i]]
                else:
                    dp[j] = dp[j]
            # print(dp)
        return dp[target]


# nums,target = [1,2,3],4
# [1, 1, 0, 0, 0]
# [1, 1, 2, 0, 0]
# [1, 1, 2, 4, 0]
# [1, 1, 2, 4, 7]
# nums,target = [9],3
# print(Solution().combinationSum4(nums,target))

# 详细解读
# https://leetcode-cn.com/problems/combination-sum-iv/solution/dai-ma-sui-xiang-lu-377-zu-he-zong-he-iv-pj9s/
