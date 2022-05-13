class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Approach 1 : brute force + hashmap, time O(n) space O(n)
        # traverse the nums, count the obj appear times
        # Approach 2 : sort ,O(nlogn)