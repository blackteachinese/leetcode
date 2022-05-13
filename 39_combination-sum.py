from typing import List


# 排列问题，讲究顺序（即 [2, 2, 3] 与 [2, 3, 2] 视为不同列表时），需要记录哪些数字已经使用过，此时用 used 数组；
# 组合问题，不讲究顺序（即 [2, 2, 3] 与 [2, 3, 2] 视为相同，此时使用 begin 变量。


class Solution:
    def combinationSum1(self, candidates: List[int], target: int) -> List[List[int]]:
        # Approach 1 : 回溯 + 剪枝
        # 搜索逻辑：递归遍历数组candidates的每个元素，每一层可以不选择index所在元素，也可以选择index所在元素
        # 如果不选择index所在元素，那么跳过改元素，下一层要index+1
        # 如果选择index所在元素，下一层还可以继续选择index不变
        # if 组合总数 == target ，记录为有效组合
        # if 组合总数 > target or candidates遍历完成，return
        def dfs(candidates,target,path,startIndex,res):
            if target == 0:
                res.append(path)
                return
            if startIndex >= len(candidates) or target < 0:
                return
            # print(res)
            dfs(candidates,target,path.copy(),startIndex+1,res)
            # 如果选取startIndex所在元素，startIndex不加1，下次还可以继续选
            dfs(candidates,target-candidates[startIndex],path + [candidates[startIndex]],startIndex,res)
        res=[]
        dfs(candidates,target,[],0,res)
        return res
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Approach 2: 回溯，搜索逻辑不一样
        # 搜索逻辑：递归遍历数组candidates的每个元素，每一层都循环遍历candidates中所有位置的元素，一层从对应的startIndex开始
        # 为了避免重复的组合，只遍历startIndex以后的元素，
        # 为了满足题意，每个元素可以重复使用，startIndex不加+1
        def dfs(candidates,target,path,startIndex,res):
            if target == 0:
                res.append(path)
                return
            if startIndex >= len(candidates) or target < 0:
                return
            for index in range(startIndex,len(candidates)):
                v = candidates[index]
                # path和target是值传递，不需要像引用传递一样，通过回溯操作还原上下文
                dfs(candidates,target-v,path + [v],index,res)
        res = []
        dfs(candidates,target,[],0,res)
        return res


# candidates,target = [2,3,6,7], 7
# candidates,target = [2,3,5], 8
# candidates,target = [2], 1

# print(Solution().combinationSum(candidates,target))