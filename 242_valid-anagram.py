class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Approach 1 : sort two string by acii , if two string is the same is anagram
        # time complexity O(nlogn)
        # Approach 2 : maintain a hashmap , iterate the first string and append count of character count in hashmap
        # iterate the second string and remove count of element ,if a coount is small than 0, return false