class Solution:
    # Approach 1 brute force
    # Approach 2 two pointer approach
    # we take two pointers,one at the beginning and one at the end of array,
    # we maintain a variable maxarea to store the maximum area 
    # at every step we find out the area formed between,
    #  move the pointer from the shorter line to the other 
    def maxArea(self, height: List[int]) -> int:
