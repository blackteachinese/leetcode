class Solution1:
    def letterCombinations(self, digits: str) -> List[str]:
        # Method1: hashmap+force iterate
        # build a hash map to store the number to alphbets
        # combinations=4*2+6*3
        # iterate the alphbet of digits
        if len(digits) == 0: return[]
        res=[]
        hashmap={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        def dfs(digits,middles):
            number = digits[0]
            a_list = hashmap[number]
            for obj in a_list:
                # add
                middles += obj
                if len(digits) >= 2:
                    # recursion
                    dfs(digits[1:],middles)
                else : # 递归到底
                    # store result
                    res.append(middles)
                # recover context
                middles = middles[:-1]
        dfs(digits,'')
        return res
     
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Method1: hashmap+force iterate
        # build a hash map to store the number to alphbets
        # combinations=4*2+6*3
        # iterate the alphbet of digits
        if len(digits) == 0: return[]
        res=[]
        hashmap={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        def dfs(index,middles):
            if index == len(digits):
                # 递归到底
                res.append(''.join(middles))
                return
            number = digits[index]
            for obj in hashmap[number]:
                # add
                middles.append(obj)
                # recursion
                dfs(index+1,middles)
                # recover context
                middles.pop()
        dfs(0,[])
        return res
     





