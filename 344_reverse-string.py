from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        l,r=0,len(s)-1
        while l < r:
            s[l],s[r] = s[r],s[l]
            l += 1
            r -= 1


# s = ["h","e","l","l","o"]
s = ["H","a","n","n","a","h"]
Solution().reverseString(s)
print(s)