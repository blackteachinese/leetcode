class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Approach 1 : brute force O(n2)
        # Approach 2 : hash. O(n)
        # we make a hashamp , put the element of nums into the hashmap
        # iterate nums and find (target - element) from the set
        # if we find the value from hashmap, return the result