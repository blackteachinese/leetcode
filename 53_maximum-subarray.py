from typing import List
class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = {}
        maxnum = dp[0] = nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(nums[i],nums[i] + dp[i -1])
            maxnum = max(maxnum,dp[i])
        return maxnum
        # 边界、特殊
        # 所有解法 9min
        # 1.暴力法：O(n^2)
        # 2.9min 缓存一个当前最大值，一个当前累计值，从正数开始累计，若累积值为负数，重新从下一个正数开发
        # 3.动态规划6min 思路失败 ：时间O(n)，空间O(n)

        # 思路：
        # 1 关键词：连续子数组，只需要最大和，可用动态规划
        # 2 因为很难确定最大的连续子数组会包含哪一个数，所以可以求出所有经过每一个数时的连续子数组的最大和，然后再取其中的最大值
        # 3 定义子问题/定义状态，
        # 假设输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
        # 子问题1：经过-2的连续子数组的最大和
        # 子问题2：经过1的连续子数组的最大和
        # 因为我们不能确定-2是连续子数组的倒数第几个元素，此时自问提是有后效性的。
        # 解决有后效性的的思路是增加定义的条件，转化为“以-2作为结尾的连续子数组的最大和”
        # 子问题1：以-2作为结尾的连续子数组的最大和
        # 子问题2：以1作为结尾的连续子数组的最大和
        # 自问题描述为状态：dp[i]表示以nums[i]结尾的连续子数组的最大和
        # 4 定义状态转移方程
        # 因为以nums[i]结尾，nums[i]一定要取。如果dp[i-1]大于0，加上dp[i-1]会更大，否则不用加。
        # 因此 dp[i] = nums[i] or dp[i] = nums[i] + dp[i-1]
        # 推导为 dp[i] = max{nums[i]},dp[i-1] + nums[i]}
        # 5 初始值
        # 第一个值dp[0]只有一个数num[0]，并且num[0]必需选上，所有dp[0] = num[0]

class Solution: 
    def maxSubArray(self, nums: List[int]) -> int:
        # 滚动数组简化空间 时间O(n)，空间O(1)
        maxnum = left = nums[0]
        right = 0
        for i in range(1,len(nums)):
            right = max(nums[i],nums[i] + left)
            maxnum = max(maxnum,right)
            left = right
        return maxnum



print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(Solution().maxSubArray([1]))
print(Solution().maxSubArray([5,4,-1,7,8]))