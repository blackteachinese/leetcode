class Solution:
    def hammingWeight1(self, n: int) -> int:
        # Approach 1 : clean the lowest digit, use  x & (x - 1) until the result is 0
        times = 0
        while n != 0:
            n &= n - 1
            times += 1
        return times

class Solution:
    def hammingWeight(self, n: int) -> int:
        # Approach 1 : iterative  n & 1; n >> 1
        times = 0
        while n != 0:
            times += n & 1
            n = n >> 1
        return times
