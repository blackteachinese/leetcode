from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Approach 1 :dfs搜索+回缩 找到所有子数组组合，比较并记录子数组组合乘积最大值
        # Approach 2 : dp
        # 非空连续子数组乘积最大值 = max(以nums[i]结尾的非空子数组的最大乘积值)
        # 以nums[i]结尾的非空子数组的最大乘积值 = max(以nums[i-1]结尾的非空子数组的最大乘积值 * nums[i] , nums[i])
        # dp[i] 以nums[i]结尾的非空子数组的最大乘积值
        # dp[i] = max{dp[i-1]*nums[i], nums[i]}
        # 最有子结构？ 因为元素存在负数，没有最有子结构

        # 我们可以根据正负性进行分类讨论,找出有最有子结构的递推公式
        # if nums[i] >= 0 , dpMax[i] = max{dpMax[i-1]*nums[i],nums[i]}, dpmin[i] = min{dpmin[i-1]*nums[i],num[i]}
        # if nums[i] < 0, dpMax[i] = max{dpmin[i-1]*nums[i],nums[i]} , dpmin[i] = min{dpMax[i-1]*nums[i],num[i]}
        # nums[i] >= 0 和 nums[i] < 0 的公式可以合并，合并后如下
        # dpMax[i] = max{dpMax[i-1]*nums[i], dpmin[i-1]*nums[i], nums[i]}
        # dpmin[i] = min{dpmin[i-1]*nums[i], dpMax[i-1]*nums[i], nums[i]}
        # !!! wrong 注意数组直接等于是引用传递
        dpMax,dpmin=[0]*len(nums),[0]*len(nums)
        # 初始化
        dpMax[0] = dpmin[0] = nums[0]
        for i in range(1,len(nums)):
            
            dpMax[i] = max(dpMax[i-1]*nums[i], dpmin[i-1]*nums[i], nums[i])
            dpmin[i] = min(dpmin[i-1]*nums[i], dpMax[i-1]*nums[i], nums[i])
            print(dpMax[i-1],nums[i],dpMax[i])
        # print(dpMax)
        return max(dpMax)

class Solution2:
    def maxProduct(self, nums: List[int]) -> int:
        curMax,curMin,res=nums[0],nums[0],nums[0]
        # Approach 3 : dp + 滚动数组优化
        for i in range(1,len(nums)):
            num = nums[i]
            print(res,num,curMax,curMin)
            curMax = curMax*num
            curMin = curMin*num
            # res历史最大，temMax从中间到末尾的最大，temMin从中间到末尾的最小
            temMax = max(curMax, curMin,num)
            temMin = min(curMax, curMin,num)
            curMax,curMin = temMax,temMin
            #存储到目前为止的最大值，历史最大值和当前最大值对比，
            res = max(res,curMax) 
        return res

# nums = [2,3,-2,4]
# nums = [-2,0,-1]
# print(Solution().maxProduct(nums))