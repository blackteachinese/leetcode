from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        #方法一：用一个额外数组 i => i+k%n,时间O(n)，空间O（n）
        l = []
        n = len(nums)
        for i in range(0,n):
            l.insert((i+k)%n, nums[i])
        for i in range(0,n):
            nums[i] = l[i]
        #方法二：用栈
class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        if len(nums) <= 1 : return
        k = k%len(nums)
        #方法三：整体reverse后，以K分割为两组，分开reverse
        def reverse(nums,f,t) -> None:
            print(f,t)
            while f < t:
                temp = nums[f]
                nums[f] = nums[t]
                nums[t] = temp
                f += 1
                t -= 1
        reverse(nums,0,len(nums)-1)
        reverse(nums,0,k-1)
        reverse(nums,k,len(nums)-1)

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105
 

n=[1,2,3,4,5,6,7]
Solution().rotate(n,3)
print(n)

n=[-1]
Solution().rotate(n,1)
print(n)

n=[1,2]
Solution().rotate(n,3)
print(n)