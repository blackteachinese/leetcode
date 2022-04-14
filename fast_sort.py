
import heapq
from typing import List 

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 1快速排序，取第K个数 O(logn) 
        # *** 快排 时间是O(n) 空间是O（1）
        print(nums)
        self.fastsort(nums,0,len(nums) - 1)
        print(nums)
        return nums[k - 1]

    def fastsort(self,q:List[int],l:int,r:int):
        # 快排,降序排序
        # 退出条件
        if l >= r:
            return
        # 1 确定分界点
        mid = int((l + r) / 2)
        midV = q[mid]
        i,j = l,r
        # 2 排序的结果是mid的左边都比mid的右边大
        while i < j:
            while q[i] > midV: #以mid为基准，寻找左边比他小的值
                i += 1
            while q[j] < midV: #以mid为基准，寻找右边比他大的值
                j -= 1
            print(q[i],midV,q[j])
            q[i],q[j] = q[j],q[i] #此时 q[i] 一定小于等于q[j]，可以直接交换
            print(q)
        # 3 递归处理左右两个区间
        self.fastsort(q,l,j)
        self.fastsort(q,j+1,r)

# !!!!!!!!!!次快速排序算法，无法解决有重复元素的输入数据
# print(Solution().findKthLargest([3,2,1,5,6,4],2))
# print(Solution().findKthLargest([3,10,12,1,2,4,9,5,6],4))
print(Solution().findKthLargest([3,9,2,10,1,8,5,6,4],2))
# print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6],4))