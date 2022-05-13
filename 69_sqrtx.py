

class Solution:
    def mySqrt(self, x: int) -> int:
        # Approach 1: iterative from x/2 to 1,
        # if obj*obj < x and (obj+1)*(obj+1) return |obj|
        # Approach 1: Binary search,
        l,r,ans = 0,x,-1
        while (l <= r):
            mid = l + (r - l) // 2
            if mid * mid > x:
                r = mid - 1
            else:
                ans = mid
                l = mid + 1
        return ans