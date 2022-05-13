class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 方法一：哈希表+从1开始遍历判断是否存在 O(n)+O(m) n是数组个数，m是遍历的整数个数
        # 方法二：排序+二分查找 O(nlogn)+O(logn)
        if len(nums) == 0:
            return 1
        hashmap = set(nums)
        for i in range(1,len(nums)+2):
            if i not in hashmap:
                return i
