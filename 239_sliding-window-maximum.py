class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Approach 1 : move forward step by step and compare the slide nums
        # store the max num obj
        # Approach 2 : maintain two pointer left and right to speed up the compare,
        # find the max element of slide and move the left pointer to the max index
        # move the slide forward , if the new element is bigger than the left one,if the right - left > k,left move to next index
        # Approach 3 : 双端队列+单调递减
        