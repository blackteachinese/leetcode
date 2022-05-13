from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 方法1：先合并为一个数组，如果数组个数是奇数，去中位值，如果是偶数，去中间两位平均值
        # border
        if len(nums1) == 0 and len(nums2) == 0 : return 0
        i1,j1,i2,j2=0,len(nums1),0,len(nums2)
        merge=[]
        while i1 < j1 or i2 < j2:
            num1=nums1[i1] if i1 < j1 else float('inf')
            num2=nums2[i2] if i2 < j2 else float('inf')
            # logic
            # print(num1,num2)
            if num1 <= num2:
                merge.append(num1)
                i1+=1
            else:
                merge.append(num2)
                i2+=1
        print(merge,i1,i2)
        # 中位数
        if len(merge)%2 == 1: #奇数
            return merge[len(merge)//2]
        else:#偶数
            return (merge[len(merge)//2] + merge[len(merge)//2 -1])/2

print(Solution().findMedianSortedArrays([1,3],[2]))
print(Solution().findMedianSortedArrays([1,2],[3,4]))
print(Solution().findMedianSortedArrays([1],[]))
print(Solution().findMedianSortedArrays([],[]))

# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

# 算法的时间复杂度应该为 O(log (m+n)) 。

#  

# 示例 1：

# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
# 示例 2：

# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
#  

#  

# 提示：

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106