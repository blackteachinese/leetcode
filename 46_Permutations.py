# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:

# Input: nums = [1]
# Output: [[1]]
 

# Constraints:

# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.



# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         def dfs(nums, size, depth, path, used, res):
#             if depth == size:
#                 res.append(path)
#                 return

#             for i in range(size):
#                 if not used[i]:
#                     used[i] = True
#                     path.append(nums[i])

#                     dfs(nums, size, depth + 1, path, used, res)

#                     used[i] = False
#                     path.pop()

#         size = len(nums)
#         if len(nums) == 0:
#             return []

#         used = [False for _ in range(size)]
#         res = []
#         dfs(nums, size, 0, [], used, res)
#         return res
# if __name__ == '__main__':
#     nums = [1, 2, 3]
#     solution = Solution()
#     res = solution.permute(nums)
#     print(res)

# 作者：liweiwei1419
# 链接：https://leetcode.cn/problems/permutations/solutions/9914/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liweiw/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums,size,depth,paths,used,result):
            # exit condition
            if size == depth:
                result.append(paths[:])
                return result
            for i in range(size):
                if used[i] == False:
                    paths.append(nums[i])
                    used[i] = True
                    dfs(nums,size,depth+1,paths,used,result)
                    # backtracking, recover the content
                    used[i] = False
                    paths.pop()
        if (len(nums)) == 0:
            return []
        used = [False for _ in range(len(nums))]
        res = []
        dfs(nums,len(nums),0,[],used,res)
        return res

if __name__ == '__main__':
    solution = Solution()
    print(solution.permute([1,3,5,7]))
    print(solution.permute([]))


    # https://leetcode.cn/problems/permutations/solutions/9914/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liweiw/