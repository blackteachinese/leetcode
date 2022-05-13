class Solution:
    def isPowerOfTwo1(self, n: int) -> bool:
        # wrong approach
        return n ==1 or n % 2 == 0

    def isPowerOfTwo(self, n: int) -> bool:
        # Feature1: 一个数 nn 是 22 的幂，当且仅当 nn 是正整数，并且 nn 的二进制表示中仅包含 11 个 11
        # Feature2: n must > 0
        # if n is pow of two , excute one time n & (n-1) == 0
        return n > 0 and (n & (n - 1)) == 0