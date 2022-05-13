from typing import List


class Solution:
    def lengthOfLIS1(self, nums: List[int]) -> int:
        # Approach 1 : dynamic programming
        # !!! wrong 因为并不一定同时存在nums[i] 和 nums[i-1]
        # DP[i] 表示nums[i]中最长递增子序列的长度
        # DP[i] = DP[i-1] if nums[i] <= nums[i-1]
        # DP[i] = DP[i-1]+1 if nums[i] > nums[i-1]
        
        # Approach 1 : dynamic programming
        # DP[i] 表示以nums[i]结尾的最长递增子序列的长度
        # res = max(DP[0:i])
        # DP[i] = max(DP[j] + 1 for j range(0,i)) if nums[i] > nums[j] and  0 <= j < i
        # O(n^2)+O(n) , n is the count of array
        dp = [1] * len(nums) # 初始化，最小为1
        for i in range(0,len(nums)):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Approach 2 : dynamic programming and binary search
        # 思路有点像Approach 1的错误定义，状态定义有变化
        # 理论1：如果nums[i] > max(nums[0:i-1])，最长序列长度加1，否则不变
        # 理论2：如果递增序列DP中的任意一个元素更小一点，那以后序列变长的可能性更大
        # DP表示当前最长序列，DP[k]表示序列第k个元素值，
        # 根据理论1：DP.append(nums[i]) if nums[i] > DP[-1]
        # 根据理论2：DP[k] = nums[i] if nums[i] < DP[-1] , 其中DP里大于nums[i]的所有元素里最小的一个就是DP[k]，根据二分法查找即可
        dp = []
        for target in nums:
            if len(dp) == 0 or target > dp[-1]:
                dp.append(target)
            else:
                l,r = 0,len(dp)-1
                pos = r
                while l <= r:
                    m = l + (r - l) // 2
                    if dp[m] < target:
                        l = m + 1
                    else:#  dp[m] >= nums[i] 
                         # 因为要找的是比略target大的值，pos设为m，而不是m+1
                        pos = m
                        r = m - 1 
                dp[pos] = target
                # print(dp)
        return len(dp)


# nums = [10,9,2,5,3,7,101,18]
# nums = [0,1,0,3,2,3]
# nums = [7,7,7,7,7,7,7]
# nums = [1]
nums=[3,5,6,2,5,4,19,5,6,7,12]

print(Solution().lengthOfLIS(nums))