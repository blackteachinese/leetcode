from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 思路：
        # 方法一：直接遍历，O(n^2)
        # 方法二：二分法+双指针
        # 时间复杂度O(logn),空间复杂度O(1)
        # 边界值
        if len(nums)==0:
            return [-1,-1]
        # 初始化
        l,m,r=0,0,len(nums)
        # 1 二分法找到target所在下标,可能不存在
        # 二分法边界情况太多，需要背模板
        while  l <= r:
            m=int(l + (r -l)/2)
            if m >= len(nums):
                return [-1,-1]
            if nums[m] == target:
                break
            elif nums[m] < target:
                l = m + 1
            else :
                r = m - 1
        # print(l,m,r)
        # 不存在target时,返回异常
        if nums[m] != target:
            return [-1,-1]
        # 2 双指针，找到左边第一个等于target的下标，右边第一个大于target的下标-1
        # 双指针从m的位置开始
        l = r = m
        while nums[l] >= target:
            l -= 1
            if l < 0:
                break
        while nums[r] <= target:
            r += 1
            if r > len(nums) - 1:
                break
        # print(l,m,r)
        rs=[]
        rs.append(l+1 if l >=0 else 0)
        rs.append(r-1 if r < len(nums) else len(nums)-1)
        return rs

# print(Solution().searchRange([5,7,7,8,8,10],6))
# print(Solution().searchRange([0,1,2,3,4,4,4],2))
# print(Solution().searchRange([1,3],1))
print(Solution().searchRange([2,2],3))